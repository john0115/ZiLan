$(document).ready(function() {
        // alert(0);
        // $("#ajaxsubmit").click(function () {
        //     alert($.cookie("csrftoken"));
        //     $.post("/login/",
        //         {
        //             id_username: $("#id_username").val(),
        //             id_password: $("#id_password").val(),
        //             ajax_status: true,
        //             // "csrfmiddlewaretoken": $.cookie('csrftoken'),
        //         },
        //         function (data) {
        //             alert(2);
        //             var datej = $.parseJSON(data);
        //             $("#mess").html(datej['mess']);
        //         });
        //
        // });
 $("#ajaxsubmit").click(function () {
        $.ajax({
            url:'http://127.0.0.1:8000/apilogin/',
            data:{
                    id_username: $("#id_username").val(),
                    id_password: $("#id_password").val(),
                    ajax_status: true,
            },

            dataType:'jsonp',//服务器返回json格式数据
            crossDomain: true,
            jsonp: 'callback',
            type:'POST',//HTTP请求类型
            timeout:10000,//超时时间设置为10秒；
            success:function(data){
                               if(data){
                                 alert("登录成功！");
                               }else{
                                 alert("登录失败！");
                               }

                             },
                             error:function(xhr,type,errorThrown){
                                  console.log(type);
                                  //alert(xhr);
                             }
            });
 });
  $("#test").click(function () {

      var delnum = $("#test").attr('value');
      // alert($("[name = 'csrfmiddlewaretoken']").attr('value'));
         $.ajax({
            url:'http://127.0.0.1:8000/apiwork/',
            data:{
                 // csrfmiddlewaretoken:$("[name = 'csrfmiddlewaretoken']").attr('value'),
                  "typename": "B"
            },
             //The type of the get
             // dataType:'jsonp',
             //The Type of To The Server
             contentType:'multipart/form-data',
            type:'GET',//HTTP请求类型
            success:function(data){
                                alert(1);
                                 result = $.parseJSON(data);
                                 alert(result[0].filename);
                             },
                             error:function(xhr,type,errorThrown){
                                  console.log(type);
                                  //alert(xhr);
                             }
            });
 });
  $(".btn-delete").click(function () {
      var id = $(this).attr('value');
      var action = $(this).attr('action');
       // alert($(this).attr('action'));
         $.ajax({
             url:action,
            data:{
                "csrfmiddlewaretoken": $.cookie('csrftoken'),
                  "id": id,
            },
            type:'POST',//HTTP请求类型
            success:function(data){
                                 alert(data['message']);
                                 window.location.reload()
                             },
                             error:function(xhr,type,errorThrown){
                                  console.log(type);
                             }
            });
 });
  $(".home-delete").click(function () {
      var id = $(this).attr('value');
      var action = $(this).attr('action');
       // alert($(this).attr('action'));
         $.ajax({
             url:action,
            data:{
                "csrfmiddlewaretoken": $.cookie('csrftoken'),
                  "id": id,
            },
            type:'POST',//HTTP请求类型
            success:function(data){
                                 alert(data['message']);
                                 window.location.reload()
                             },
                             error:function(xhr,type,errorThrown){
                                  console.log(type);
                             }
            });
 });
   $("#type").change(function () {
             // var id=$("#type").find("option:selected").attr('value');
             // location.href=this.options[this.selectedIndex].value

   });

});