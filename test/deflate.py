# -*- coding: utf-8 -*-
import zlib
import base64


s = '''


<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>猎头顾问注册_猎聘网：LiePin.com</title>
<!--#set var='compatible' value=''-->
<meta http-equiv="X-UA-Compatible" content="IE=11; IE=10; IE=9; IE=8; IE=7; IE=EDGE" />
<link rel="icon" href="http://s.lietou-static.com/r/164123/images/favicon.ico" type="image/x-icon" />
<script>function FileManagerClass(){return this.bad=null,this.root="http://s.lietou-static.com/",this.cache={},this.init(),this}FileManagerClass.prototype.init=function(){return/(^|\s|;)cdnbad\s*=\s*1($|\s|;)/.test(document.cookie)?this.bad=!0:document.write(unescape('%3Cscript src="'+this.root+'js/cdntest.js?'+~(-new Date()/6e5)+'" type="text/javascript"%3E%3C/script%3E')),this},FileManagerClass.prototype.fetchCDN=function(){var t;return null===this.bad&&(t=new Date,t.setTime(t.getTime()+864e5),document.cookie="cdnbad=1;expires="+t.toGMTString()+";path=/;domain=liepin.com",this.bad=!0,this.root="http://i.s.lietou-static.com/"),this},FileManagerClass.prototype.get=function(){var t,e,s,i=arguments;for(s=0;s<i.length;s++)e=0===i[s].indexOf("http")?i[s]:this.root+(0===i[s].indexOf("/")?i[s].substring(1):i[s]),this.cache[e]||(this.cache[e]=!0,t=i[s].substring(i[s].lastIndexOf(".")+1),-1!==t.indexOf("?")&&(t=t.substring(0,t.indexOf("?"))),"css"===t?document.write(unescape('%3Clink href="'+e+'" rel="stylesheet" type="text/css"/%3E')):"js"===t&&document.write(unescape('%3Cscript src="'+e+'"%3E%3C/script%3E')));return this};var FileManager=new FileManagerClass;</script>
<script>FileManager.fetchCDN();</script>
<!--[if lt IE 9]>
<script type="text/javascript">FileManager.get('/r/164123/article/beta2/js/html5shiv.js');</script>
<![endif]-->
<!--[if IE 6]>
<script type="text/javascript">FileManager.get('/r/164123/article/beta2/js/DD_belatedPNG.js');</script>
<script>DD_belatedPNG.fix('.pngfix');</script>
<![endif]-->
<script>FileManager.get('/r/181907/p/beta2/css/common.css','/r/180770/p/beta2/css/public.css','/r/181500/p/beta2/js/jquery-1.7.1.min.js','/r/182279/p/beta2/js/lt.core.js','/r/164123/p/beta2/js/plugins/jquery.artDialog.js','/r/177806/p/beta2/js/plugins/jquery.loadingui.js','/r/164123/p/beta2/js/plugins/jquery.tipsui.js','/r/181252/p/beta2/js/lt.apps.js');</script>
<script type="text/javascript">
var HeaderHelperConfig = {
  pageType: 1
};
</script>
</head>
<body id="user-regh">
<!--#set var='compatible' value=''-->
<script type="text/javascript">FileManager.get('/r/177535/p/beta2/css/header.css');</script>
<header id="header-p-beta2">
  <div class="header">
    <div class="wrap">
      <div class="logo">
        <a href="http://www.liepin.com/" target="_blank"><img alt="猎聘网logo" class="pngfix" src="http://s.lietou-static.com/r/164123/p/beta2/images/logo.png" width="110" height="40" /><em><i class="icons16 icons16-home-white" title="首页"></i></em></a>
      </div>
      <div class="quick-menu"></div>
    </div>
  </div>
</header>
<script type="text/javascript">FileManager.get('/r/180036/p/beta2/js/header.js');</script>
<div class="container">
	<div class="wrap">
    	<div class="user-login-reg ui-tab-panel">
      		<div class="ui-tab-control">
        		<ul class="clearfix">
          			<li class="active" data-name="hregist">猎头顾问注册</li>
          			<li data-name="hlogin">猎头顾问登录</li>
        		</ul>
      		</div>
      		<div class="ui-tab-container">
        		<div class="ui-tab-toggle hide">
          		<form action="/user/ajaxlogin/" method="post" class="login-form" autocomplete="off">
            		<div>
              			<input name="user_login" class="text input-xlarge" type="text" validate-title="登录邮箱" validate-rules="['required','email']" value="" placeholder="请输入登录邮箱">
            		</div>
		            <div>
		              	<input name="user_pwd" class="text input-xlarge" type="password" validate-title="密码" validate-rules="['required']" value="" placeholder="请输入登录密码">
		            </div>
            		<div class="optional">
              			<div class="clearfix">
                			<a class="link-findpwd" href="http://www.liepin.com/passport/forgetPwd/" target="_blank">找回密码</a>
                			<label><input type="checkbox" name="chk_remember_pwd" value="on" checked="checked" class="checkbox"> 下次自动登录</label>
              			</div>
            		</div>
            		<div class="actions">
              			<input type="submit" class="btn btn-warning" name="tijiao" value="立即登录" />
            		</div>
          		</form>
        		</div>
        		<div class="ui-tab-toggle">
          		<form action="/user/ajaxregh" method="post" class="reg-form" autocomplete="off">
           		<input type="hidden" name="inviteHId" value=""/>
           		<input type="hidden" name="user_kind" value="2"/>
            		<div>
              			<input name="h_name" class="text input-xlarge" type="text" data-selector="username" validate-title="真实姓名" validate-rules="['required',['cn','$必须由汉字组成'],['length',{'max':5,'min':2},'$长度必须介于 2 位和 5 位之间']]" placeholder="请填写中文真实姓名">
            		</div>
		            <div>
		              	<input name="user_login" class="text input-xlarge" type="text" data-selector="email" validate-title="登录邮箱" validate-rules="['required','email']" value="" placeholder="请填写有效邮箱，用以登录网站">
		            </div>
		            <div>
		              	<input name="user_pwd" class="text input-xlarge" type="password" data-selector="password" validate-title="密码" validate-rules="[['required','请输入$'],['pattern',/^[0-9a-zA-Z]+$/,'$只能用字母和数字'],['length',{'min':4,'max':16},'$1长度不能$2$3']]" placeholder="密码(4-16位字母、数字，无空格)">
		            </div>
		            <div>
		              	<input name="h_tel" class="text input-xlarge" type="text" data-selector="mobile" validate-title="手机号码" validate-rules="['required','mobile']" placeholder="请填写手机号码">
		            </div>
		            <div class="control-group optional">
		              	<div>
		                	<label validate-title="《猎聘网用户服务协议》" validate-rules="[['required',{'min': 1},'请选择接受$才可注册']]" validate-group="checkbox"><input type="checkbox" class="checkbox" name="chk_agreement" value="on" checked="checked"> 接受用户协议</label>
		              	</div>
		            </div>
		            <div class="actions">
		              	<input type="submit" class="btn btn-warning" name="btn" value="立即注册" />
		            </div>
          		</form>
        		</div>
     		</div>
		</div>
	</div>
</div>
<div class="wrap">
	<ul class="column clearfix">
    	<li>
      	<dl>
	        <dt><i class="icon-reg-h icon-dlld"></i></dt>
	        <dd>
	      		<div class="title"><strong>大猎论道</strong></div>
	          	<div class="sub-title">猎头名家谈行业发展</div>
	          	<div class="desc">这里聚集着全国最优秀的猎头，这里有着最有价值的见解。</div>
	          	<div class="btn-box"><a class="btn btn-primary" href="http://h.liepin.com/dlld/" target="_blank">查看详情</a></div>
	        </dd>
      	</dl>
    	</li>
    	<li>
      		<dl>
        		<dt><i class="icon-reg-h icon-tdwd"></i></dt>
        		<dd>
		     		<div class="title"><strong>同道问答</strong></div>
		          	<div class="sub-title">资深顾问在线交流</div>
		          	<div class="desc">中国最大的职场交流平台，无数话题成为行业热点。</div>
		          	<div class="btn-box"><a class="btn btn-primary" href="http://article.liepin.com/" target="_blank">参与交流</a></div>
        		</dd>
      		</dl>
    	</li>
    	<li class="nobd">
      		<dl>
        		<dt><i class="icon-reg-h icon-clt"></i></dt>
        		<dd>
          			<div class="title"><strong>诚猎通</strong></div>
		          	<div class="sub-title">猎头公司效率工具</div>
		          	<div class="desc">猎头公司高效的曝光途径，管理下属 顾问的高效工具。 </div>
		          	<div class="btn-box"><a class="btn btn-primary" href="http://clt.liepin.com/" target="_blank">马上开通</a></div>
        		</dd>
      		</dl>
    	</li>
	</ul>
</div>
<!--#set var='compatible' value=''-->
<script type="text/javascript">FileManager.get('/r/175187/p/beta2/css/footer.css');</script>
<footer id="footer-p-beta2">
  <hr />
  <div class="wrap">
    <div class="copyright">
      <div class="copy-side">
        服务热线 (免长话费)<br /><strong>400-6838-789</strong><br /><small>工作日 9:00-19:00</small>
      </div>
      <div class="copy-main">
        <div class="item">
          <dl>
            <dt>简介</dt>
            <dd><a href="http://www.liepin.com/about/introduction.shtml" target="_blank" rel="nofollow">猎聘网简介</a></dd>
            <dd><a href="http://www.liepin.com/about/productsandservices.shtml" target="_blank" rel="nofollow">产品服务</a></dd>
            <dd><a href="http://www.liepin.com/about/innovation.shtml" target="_blank" rel="nofollow">创新优势</a></dd>
            <dd><a href="http://www.liepin.com/about/weblink/" target="_blank" rel="nofollow">友情链接</a></dd>
            <dd><a href="http://www.liepin.com/about/about_us.shtml" target="_blank" rel="nofollow">联系我们</a></dd>
          </dl>
        </div>
        <div class="item">
          <dl>
            <dt>帮助</dt>
            <dd><a href="http://www.liepin.com/help/" target="_blank" rel="nofollow">经理人帮助</a></dd>
            <dd><a href="http://www.liepin.com/help/itemlist/2/0" target="_blank" rel="nofollow">用户注册</a></dd>
            <dd><a href="http://www.liepin.com/help/itemlist/3/0" target="_blank" rel="nofollow">关于您的简历</a></dd>
            <dd><a href="http://www.liepin.com/help/itemlist/4/0" target="_blank" rel="nofollow">关于猎头</a></dd>
            <dd><a href="http://www.liepin.com/help/itemlist/5/0" target="_blank" rel="nofollow">关于职位</a></dd>
          </dl>
        </div>
        <div class="item">
          <dl>
            <dt>共赢</dt>
            <dd><a href="http://www.liepin.com/cooperation.shtml" target="_blank" rel="nofollow">网站合作</a></dd>
            <dd><a href="http://www.liepin.com/user/agreement.shtml" target="_blank" rel="nofollow">用户协议</a></dd>
            <dd><a href="http://www.liepin.com/sitemap.shtml" target="_blank" rel="nofollow">网站地图</a></dd>
            <dd><a href="http://www.liepin.com/user/feedback/" target="_blank" rel="nofollow">意见反馈</a></dd>
            <dd><a href="http://www.liepin.com/inshr/index.shtml" target="_blank" rel="nofollow">加入猎聘网</a></dd>
          </dl>
        </div>
        <div class="item">
          <dl>
            <dt>导航</dt>
            <dd><a href="http://www.liepin.com/sitemap.shtml" target="_blank" rel="nofollow">地图首页</a></dd>
            <dd><a href="http://www.liepin.com/sitemap/chengshi.shtml" target="_blank" rel="nofollow">城市分类</a></dd>
            <dd><a href="http://www.liepin.com/sitemap/hangye.shtml" target="_blank" rel="nofollow">行业分类</a></dd>
            <dd><a href="http://www.liepin.com/sitemap/zhineng.shtml" target="_blank" rel="nofollow">职能分类</a></dd>
            <dd><a href="http://www.liepin.com/sitemap/zhuceqiye.shtml" target="_blank" rel="nofollow">企业名录</a></dd>
          </dl>
        </div>
        <div class="item item-weibo">
          <a href="http://weibo.com/lietouwang" target="_blank" rel="nofollow"><i class="weibo"></i></a>
          <p>猎聘微博</p>
          <a class="btn-sina" href="http://weibo.com/lietouwang" target="_blank" rel="nofollow"></a>
        </div>
        <div class="item item-apps">
          <i class="mishu"></i>
          <p>猎聘秘书APP</p>
        </div>
      </div>
    </div>
  </div>
  <div class="copy-footer">
    <p>京ICP备09083200号 京ICP证070419号 人才服务许可证:RC0710280 京公网安备11010802012824</p>
    <p>Copyright&copy;2000-2014 liepin.com All Rights Reserved</p>
  </div>
</footer>
<script type="text/javascript">
  FileManager.get('/r/177806/p/beta2/js/page/user.regh.js');
</script>
<script type="text/javascript">window.FileManager&&FileManager.get('/r/164123/js/common/statistic/stat.js');</script>
<script>var _hmt=_hmt||[];(function(){var hm=document.createElement("script");hm.src="//hm.baidu.com/hm.js?a2647413544f5a04f00da7eee0d5e200";var s=document.getElementsByTagName("script")[0];s.parentNode.insertBefore(hm,s);})();</script> 
</body>
</html>'''

def decode_base64_and_inflate( b64string ):
    decoded_data = base64.b64decode( b64string )
    return zlib.decompress( decoded_data , -15)

def deflate_and_base64_encode( string_val ):
    zlibbed_str = zlib.compress( string_val )
    # compressed_string = zlibbed_str[2:-4]
    return base64.b64encode( zlibbed_str )

print deflate_and_base64_encode(s)