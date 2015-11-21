# qiniu-upload
七牛上传token相关

## 文件介绍

### /create/ 七牛上传token生成

* 算法
	* 将上传策略序列化成为json格式：json_text
	* 对json序列化后的上传策略进行URL安全的Base64编码：urlsafe_base64_text
	* 用secret_key对编码后的上传策略进行HMAC-SHA1加密，并且做URL安全的Base64编码：HMAC_SHA1_text
	* 将 access_key、HMAC_SHA1_text 和 urlsafe_base64_text 用 “:” 连接起来,得到UploadToken。

#### python/create_token.py

* 必须参数
	* access_key
	* secret_key
	* scope //上传空间
	* deadline token //有效时间（时间戳格式）

#### js/create_token.js

* 必须参数
	* access_key
	* secret_key
	* scope //上传空间
	* deadline token //有效时间（时间戳格式）
* 内部引用了CryptoJS