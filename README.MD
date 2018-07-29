随着各种字幕网站的关停，找外挂字幕越来越麻烦

后来发现迅雷影音的在线字幕匹配功能非常好用

但是更喜欢PotPlay播放器+Zune皮肤的我很不喜欢迅雷影音的播放功能

于是尝试逆向出迅雷影音的字幕搜索API

折腾了几个小时，终于搞定，暂时做个半成品，代码很简单，有兴趣的小伙伴可以自己用其他语言实现

做了个简单的字幕下载小工具给自己用，一开始使用Electron，但是打包之后占用空间居然达到了100M

于是后来用C#写了个WPF版本，需要下载可以直接查看release，已经打包

[下载页面](https://github.com/DCjanus/ThunderSubs/releases)

[流程解析](https://blog.dcjanus.com/posts/api_for_xunlei_subscene/)

# 其他版本

感谢[weaming](https://github.com/weaming)提供的Python命令行版： <https://github.com/weaming/thunder-subtitle>
