using System;
using System.IO;
using System.Threading.Tasks;
using System.Net;
using Newtonsoft.Json;
using System.Security.Cryptography;
using System.Linq;
using System.Text;

namespace DC_sub_downloader
{
    public class SubDownloader
    {
        private String filePath;
        public SubDownloader(String filePath)
        {
            this.filePath = filePath;
        }

        public async Task<int> downLoadAllAsync()
        {
            var dirName = Path.GetDirectoryName(this.filePath);
            var fileNameWithoutExtension = Path.GetFileNameWithoutExtension(this.filePath);
            var client = new WebClient();

            var subInfoList = await this.getSubInfoListAsync();
            subInfoList = subInfoList.Where(s => s.rate > 0).ToArray();

            for (var i = 0; i < subInfoList.Length; i++)
            {
                var theSubInfo = subInfoList[i];
                var subFileName = String.Format("{0}_{1}{2}", fileNameWithoutExtension, i, Path.GetExtension(theSubInfo.surl));
                var subFilePath = Path.Combine(dirName, subFileName);
                while (true)
                {
                    try
                    {
                        await client.DownloadFileTaskAsync(theSubInfo.surl, subFilePath);
                        break;
                    }
                    catch (WebException)
                    {
                        continue;
                    }
                }
            }
            return subInfoList.Length;
        }

        public String Cid
        {
            get
            {
                var stream = new FileStream(this.filePath, FileMode.Open, FileAccess.Read);
                var reader = new BinaryReader(stream);
                var fileSize = (new FileInfo(filePath).Length);
                var SHA1 = new SHA1CryptoServiceProvider();
                var buffer = new byte[0xf000];
                if (fileSize < 0xf000)
                {
                    reader.Read(buffer, 0, (int)fileSize);
                    buffer = SHA1.ComputeHash(buffer, 0, (int)fileSize);
                }
                else
                {
                    reader.Read(buffer, 0, 0x5000);
                    stream.Seek(fileSize / 3, SeekOrigin.Begin);
                    reader.Read(buffer, 0x5000, 0x5000);
                    stream.Seek(fileSize - 0x5000, SeekOrigin.Begin);
                    reader.Read(buffer, 0xa000, 0x5000);

                    buffer = SHA1.ComputeHash(buffer, 0, 0xf000);
                }
                var result = "";
                foreach (var i in buffer)
                {
                    result += String.Format("{0:X2}", i);
                }
                return result;
            }
        }

        public async Task<String> getRawSubInfosAsync()
        {
            var client = new WebClient();
            var url = String.Format("http://sub.xmp.sandai.net:8000/subxl/{0}.json", this.Cid);
            while (true)
            {
                try
                {
                    var data = await client.DownloadDataTaskAsync(url);
                    return Encoding.UTF8.GetString(data);
                }
                catch (WebException)
                {
                    continue;
                }
            }
        }

        public async Task<SubInfo[]> getSubInfoListAsync()
        {
            var result = JsonConvert.DeserializeObject<SubList>(await this.getRawSubInfosAsync()).sublist;
            result = result.Where(s => !string.IsNullOrEmpty(s.surl)).ToArray();
            return result;
        }


    }
    public class SubInfo
    {
        public String scid { get; set; }
        public String sname { get; set; }
        public String language { get; set; }
        public long rate { get; set; }
        public String surl { get; set; }
        public long svote { get; set; }
        public long roffset { get; set; }
    }
    public class SubList
    {
        public SubInfo[] sublist;
    }
}
