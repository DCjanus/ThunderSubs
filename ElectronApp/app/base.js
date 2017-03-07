var crypto = require("crypto");
var fs = require("fs");
var buffer = require("buffer");
var request = require('request');
var path = require("path");
exports.cid_hash_file = cid_hash_file;
exports.get_sub_info_list = get_sub_info_list;
exports.processOneMovie = processOneMovie;

function cid_hash_file(file_path) {
    var file_size = fs.statSync(file_path).size;
    var the_file = fs.openSync(file_path, "r");
    var sha1_hasher = crypto.createHash("sha1");
    if (file_size < 0xf000) {
        var buffer = new Buffer(file_size);
        fs.readSync(the_file, buffer, 0, file_size, 0);
        sha1_hasher.update(buffer);
    } else {
        var buffer = new Buffer(0x5000);
        fs.readSync(the_file, buffer, 0, 0x5000, 0);
        sha1_hasher.update(buffer);

        fs.readSync(the_file, buffer, 0, 0x5000, parseInt(file_size / 3));
        sha1_hasher.update(buffer);

        fs.readSync(the_file, buffer, 0, 0x5000, file_size - 0x5000);
        sha1_hasher.update(buffer);
    }
    fs.close(the_file);
    return sha1_hasher.digest("HEX").toUpperCase();
}

function get_sub_info_list(cid, callback) {
    var url = "http://sub.xmp.sandai.net:8000/subxl/" + cid + ".json";
    result = null;
    request.get(url, function (err, respone, body) {
        if (respone.statusCode == 200) {
            var sublist = JSON.parse(body).sublist;
            sublist = sublist.filter((value, index, array) => {
                for (var name in value) {
                    return true;
                }
                return false;
            })
            callback(sublist);
        } else {
            get_sub_info_list(cid, callback);
        }
    })
}

function processOneMovie(file) {
    var cid = cid_hash_file(file.path);
    get_sub_info_list(cid, sublist => {
        var sub_type_map = build_sub_type_map(sublist);
        sub_type_map.forEach((item, index, theMap) => {
            item.forEach((item, index, array) => {
                downloadOneSub(item, index, file);
            });
        });
    })
}

function downloadOneSub(sub_info, index, file) {
    if (sub_info.rate === "0") {
        return;
    }

    var target_dir = path.dirname(file.path);
    var movie_extname = path.extname(file.path);
    var movie_name = path.basename(file.path, movie_extname);
    var sub_extname = sub_info.surl.split(".").pop();

    if (index === 0) {
        var sub_file_name = movie_name + "." + sub_extname;
    } else {
        var sub_file_name = movie_name + index + "." + sub_extname;
    }
    var sub_file_path = path.join(target_dir, sub_file_name);
    var my_request = request.get(sub_info.surl);
    my_request
        .on('error', (err) => {
            downloadOneSub(sub_info, index, file);
        })
        .on('response', (respone) => {
            if (respone.statusCode == 200) {
                my_request.pipe(fs.createWriteStream(sub_file_path));
            } else {
                downloadOneSub(sub_info, index, file);
            }
        })
}

function build_sub_type_map(sublist) {
    var result = new Map();
    for (var sub_info of sublist) {
        var sub_type = sub_info.surl.split(".").pop();
        if (result.has(sub_type)) {
            result.get(sub_type).push(sub_info);
        } else {
            result.set(sub_type, new Array(sub_info));
        }
    }
    return result;
}