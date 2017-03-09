using System;
using System.Linq;

using System.Windows;
using System.IO;

namespace DC_sub_downloader
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            this.AllowDrop = true;
        }

        private async void Window_Drop(object sender, DragEventArgs e)
        {
            var allFilePaths = (String[])e.Data.GetData(DataFormats.FileDrop);
            var downloadInfoList = allFilePaths.Select(x => new DownloadInfo() { fileName = System.IO.Path.GetFileName(x), status = DownloadStatus.Pre, subNumber = 0 }).ToArray();

            this.messageBlock.Text = String.Join("\n", downloadInfoList.Select(x => x.message));

            for (var i = 0; i < allFilePaths.Length; i++)
            {
                var filePath = allFilePaths[i];
                if (File.Exists(filePath))
                {
                    var theDownloader = new SubDownloader(filePath);

                    downloadInfoList[i].status = DownloadStatus.Ing;
                    this.messageBlock.Text = String.Join("\n", downloadInfoList.Select(x => x.message));

                    var subNumber = await theDownloader.downLoadAllAsync();

                    downloadInfoList[i].subNumber = subNumber;
                    downloadInfoList[i].status = DownloadStatus.Done;
                }
                else
                {
                    downloadInfoList[i].status = DownloadStatus.NotFile;
                }
                this.messageBlock.Text = String.Join("\n", downloadInfoList.Select(x => x.message));
            }
        }

        private void Window_DragEnter(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                e.Effects = DragDropEffects.Link;
            }
            else
            {
                e.Effects = DragDropEffects.None;
                this.messageBlock.Text = "拖入的不是文件";
            }
        }

        private void Window_DragOver(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                e.Effects = DragDropEffects.Link;
            }
            else
            {
                e.Effects = DragDropEffects.None;
            }
        }
    }

    enum DownloadStatus
    {
        Pre, Ing, Done, NotFile
    }

    class DownloadInfo
    {
        public String fileName;
        public DownloadStatus status;
        public int subNumber;
        public String message
        {
            get
            {
                if (status == DownloadStatus.Pre)
                {
                    return String.Format("即将开始下载:{0}", fileName);
                }
                else if (status == DownloadStatus.Ing)
                {
                    return String.Format("正在下载字幕:{0}", fileName);
                }
                else if (status == DownloadStatus.NotFile)
                {
                    return String.Format("不是文件或者文件无法访问:{0}", fileName);
                }
                else
                {
                    return String.Format("{1,2}个字幕完成：{0}", fileName, subNumber);
                }
            }
        }
    }
}
