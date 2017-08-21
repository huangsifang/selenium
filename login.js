
	var pgeditorChar = new PGEdit({
	    pgePath: "/bsplatform/webdocs/ocx/",//控件文件路径
		pgeId: "_ocx_passwordChar",//控件ID
		pgeRandomNum:"09114386172767518930232410527842",//随机数
		pgeEdittype: 0,//控件类型,0星号,1明文
		pgeEreg1: "[\\s\\S]*",//输入过程中字符类型限制，如果只允许输入纯数字，如："[0-9]*",
		pgeEreg2: "[\\s\\S]{6,12}",	//输入完毕后字符类型判断条件，如果只允许输入纯数字，如："[0-9]{6,6}",
		pgeMaxlength: 12,//允许最大输入长度
		pgeTabindex: 2,//tab键顺序
		pgeClass: "cinput",//控件css样式
		pgeInstallClass: "cinput",//控件css样式
		tabCallback:"randCode",//火狐控件Tab键回调,设置要跳转到的ID
		pgeOnkeydown:""//回车键响应函数
	});

	var pgeditorChar2 = new PGEdit({
	    pgePath: "/bsplatform/webdocs/ocx/",//控件文件路径
		pgeId: "_ocx_passwordChar2",//控件ID
		pgeRandomNum:"09114386172767518930232410527842",//随机数
		pgeEdittype: 0,//控件类型,0星号,1明文
		pgeEreg1: "[\\s\\S]*",//输入过程中字符类型限制，如果只允许输入纯数字，如："[0-9]*",
		pgeEreg2: "[\\s\\S]{6,12}",	//输入完毕后字符类型判断条件，如果只允许输入纯数字，如："[0-9]{6,6}",
		pgeMaxlength: 12,//允许最大输入长度
		pgeTabindex: 2,//tab键顺序
		pgeClass: "cinput",//控件css样式
		pgeInstallClass: "cinput",//控件css样式
		tabCallback:"randCode",//火狐控件Tab键回调,设置要跳转到的ID
		pgeOnkeydown:""//回车键响应函数
	});

	$(document).ready( function() {
		$("#uid").focus();
		var error = $(".zb_dlmrightprompt").html();
		if(error==""){
		$(".zb_dlmrightprompt").hide();
		}else{
		$(".zb_dlmrightprompt").show();
		}
		
		pwdTab("gform");
		
   		//pgeditorChar.pgInitialize();//初始化控件，或者放到</body>前边		
		//pgeditorChar2.pgInitialize();
	
		var lastUser = $.cookie("MLastLogin");
		if (lastUser != "") {
			$("#uid").val(lastUser);
		}
		$("#loginBt").attr("disabled", false);
		$("#loginBt").css("cursor", "pointer");

		$(":input").keydown( function(e) {
			var curKey = e.which;
			if (curKey == 13) {
				$("#loginBt").click();
				return false;
			}
		});
		$(".login_tab").find("span").click( function() {
			$("form").hide();
			$("span").attr("class", "");
			$(this).attr("class", "on");
			$("#" + $(this).attr("formId")).show();
		});
	});
	
	function display(id){
		$("#"+id).addClass("current");
		$("#"+id+"_con").css("display","block");
	}
	
	function disappear(id){
		$("#"+id).removeClass("current");
		$("#"+id+"_con").css("display","none");
	}
		
	function pwdTab(formId){
		if($("#kjflag","#"+formId).attr("checked")){
			$("#pwd_kl","#"+formId).css("display","none");
			$("#pwd_kj","#"+formId).css("display","");
			if("gform" == formId){
				pgeditorChar.pgInitialize();
			}else{
				pgeditorChar2.pgInitialize();
			}
		}else{
			$("#pwd_kl","#"+formId).css("display","");
			$("#pwd_kj","#"+formId).css("display","none");
		}
	}
		
		
	function head_search()
	{
		var num = document.getElementById("snum").value;
		var url = document.getElementById("actionUrl").value;
		//如果用户没有输入查询条件，则在查询前清空文本框中的初始内容
		search_check(document.getElementById("flag"));
		var flag = encodeURIComponent(encodeURIComponent($("#flag").val()));
		if(num == '0')
		{
			url = ""+url+"?title="+flag;
		}	
		if(num == '1')
		{
			url = "/bsplatform"+url+"?storename="+flag+"&grade=all";
		}
		if(num == '2')
				{
					
					url = "http://www.l-zzz.com/plastic/price_datax.jsp?keyword="+flag.toUpperCase()+"&jsgjz=&snum=2&txtKeywords1=&phid="+flag.toUpperCase()+"&xhgetid=1";
				}
				if(num == '3')
				{
					url = "http://www.l-zzz.com/xhinfo/serchxn1.jsp?keyword="+flag.toUpperCase()+"&jsgjz=&snum=3&txtKeywords1=&phid=&xhgetid=1&txtSign="+flag;
				}
		if(num == '4')
		{
			url = "/lineQuery.do?keyadd="+flag;
		}
		window.location.href = url;
	}
		
		
	function onclickimg() {
		var d = new Date().getTime();
		document.getElementById("img_rand_code").src = "/bsplatform/authimg.img?aa=" + d;
	}
	
	function forgetPwd() {
		window.location.href = "/bsplatform/bsp/menber/findpwd/index.do";
	}
	
	function doLogin(formId) {
		var oForm = $("#" + formId);
		var username = oForm.find("#uid").val();
		//var password = oForm.find("#pwd").val();
		var gdkeyid = oForm.find("#randCode").val();
		var type = oForm.find("#type").val();
		
		var url = oForm.find("#url").val();
		
		// 密码方式：1 常规密码登录，2 控件密码登录
		var pwdTyp = "1";
		if($("#kjflag","#"+formId).attr("checked")){
			pwdTyp = "2";
		}
		
		if ("1" == type) {
			if ("" == username) {
				alert("请输入用户名!");
				$("#uid").focus();
				return false;
			}
			if(pwdTyp == "1"){
				if($("#kl").val() == ""){
					alert("请输入密码");
					$("#kl","#"+formId).focus();
					return false;
				}
			}else{
				if(pgeditorChar.pwdLength()==0){
				     alert("请输入密码");
				     $("#_ocx_passwordChar").focus();
					 return false;
				}
				if(pgeditorChar.pwdValid()==1){
					alert("密码不符合要求");
					$("#_ocx_passwordChar").focus();
					return false;
				}
			}
			
			if (gdkeyid == "") {
				alert("请输入验证码!");
				$("#randCode").focus();
				return false;
			}
			$("#rememberflag").val($("#checkbox").attr("checked") ? "1" : "0");
		}else{
			if ("" == username) {
				alert("请选择证书!");
				return false;
			}
			
			if(pwdTyp == "1"){
				if(oForm.find().val("#kl") == ""){
					alert("请输入密码");
					$("#kl","#"+formId).focus();
					return false;
				}
			}else{
				if(pgeditorChar2.pwdLength()==0){
				     alert("请输入密码");
				     $("#_ocx_passwordChar2").focus();
					 return false;
				}
			
				if(pgeditorChar2.pwdValid()==1){
					alert("密码不符合要求");
					$("#_ocx_passwordChar2").focus();
					return false;
				}
			}
		}
		
		
		if ("1" == type) {
			if(pwdTyp == "1"){
				var kl = oForm.find("#kl").val();
				oForm.find("#pwd").val(gScript.getPwdMd5(kl, "/bsplatform", "1"));
			}else{
				var PwdResultChar = pgeditorChar.pwdResult();//获得密码密文
				oForm.find("#pwd").val(PwdResultChar);
			}
		}else{
			if(pwdTyp == "1"){
				var kl = oForm.find("#kl").val();
				oForm.find("#pwd").val(gScript.getPwdMd5(kl, "/bsplatform", "1"));
			}else{
				var PwdResultChar2 = pgeditorChar2.pwdResult();//获得密码密文
				oForm.find("#pwd").val(PwdResultChar2);
			}
		}
		
		oForm.find("#url").val(encodeURI(url));
		oForm.find("#loginBt").attr("disabled", true).css("cursor", "default");
		//清空明文密码
		$("#kl").val("");
		oForm.submit();
		return false;
	}

	function checkForm(form) {
		var index = form.CertList.value;
		if (index == -1) {
			alert("没有找到证书,请申请安装证书!");
			return false;
		}
		var signedData = signLogonData(arrayCerts[index], form.ToSign);
		if (signedData.length > 0) {
			form.SignedData.value = signedData;
			return true;
		}
		alert("证书验证签名失败!");
		return false;
	}

	function selectCert(obj) {
		var index = $(obj).find("option:selected").val();
		if (!index || -1 == index) {
			//无证书 
			return;
		}
		$("#IssuerDN").text(arrayCerts[index].Issuer);
		$("#CertDN").text(arrayCerts[index].Subject);
		$("#CertSerial").text(arrayCerts[index].SerialNumber);
		$("#CertValid").text(
				new Date(arrayCerts[index].ValidFrom).toLocaleString() + " 至 "
						+ new Date(arrayCerts[index].ValidTo).toLocaleString());
		// 证书+口令登录方式
		LogonForm.uid.value = arrayCerts[index].CommonName;
		var subjectNames = new Names(arrayCerts[index].Subject);
		if (subjectNames.getItem("SN") != null) {
			LogonForm.uid.value = subjectNames.getItem("SN");
		} else {
			LogonForm.uid.value = "";
		}
	}
	function certView2(form) {
		if (arrayCerts.length > 0) {
			var index = document.all.CertList.value;
			arrayCerts[index].View();
		}
	}

