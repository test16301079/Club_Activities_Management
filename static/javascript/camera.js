
     var video = document.querySelector('video');
     var text = document.getElementById('text');

     var canvas1 = document.querySelector('#canvasRect');
     var context1 = canvas1.getContext('2d');
     var img = document.getElementById('img');
     var mediaStreamTrack;


     // 一堆兼容代码
     window.URL = (window.URL || window.webkitURL || window.mozURL || window.msURL);
     if (navigator.mediaDevices === undefined) {
        navigator.mediaDevices = {};
     }
     if (navigator.mediaDevices.getUserMedia === undefined) {
     navigator.mediaDevices.getUserMedia = function(constraints) {
        var getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
      if (!getUserMedia) {
        return Promise.reject(new Error('getUserMedia is not implemented in this browser'));
      }
        return new Promise(function(resolve, reject) {
                getUserMedia.call(navigator, constraints, resolve, reject);
             });
        }
     }

     //摄像头调用配置
     var mediaOpts = {
     audio: false,
     video: true,
     video: { facingMode: "environment"} // 或者 "user"
     // video: { width: 1280, height: 720 }
     // video: { facingMode: { exact: "environment" } }// 或者 "user"
     }
     // 一堆兼容代码
     window.URL = (window.URL || window.webkitURL || window.mozURL || window.msURL);
     if (navigator.mediaDevices === undefined) {
        navigator.mediaDevices = {};
     }
     if (navigator.mediaDevices.getUserMedia === undefined) {
     navigator.mediaDevices.getUserMedia = function(constraints) {
        var getUserMedia = navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
      if (!getUserMedia) {
        return Promise.reject(new Error('getUserMedia is not implemented in this browser'));
      }
        return new Promise(function(resolve, reject) {
                getUserMedia.call(navigator, constraints, resolve, reject);
             });
        }
     }

     //摄像头调用配置
     var mediaOpts = {
     audio: false,
     video: true,
     video: { facingMode: "environment"} // 或者 "user"
     // video: { width: 1280, height: 720 }
     // video: { facingMode: { exact: "environment" } }// 或者 "user"
     }

     // 回调
     function successFunc(stream) {
         mediaStreamTrack = stream;
         video = document.querySelector('video');
        if ("srcObject" in video) {
          video.srcObject = stream
         } else {
            video.src = window.URL && window.URL.createObjectURL(stream) || stream
         }
         video.play();
     }
     function errorFunc(err) {
         alert(err.name);
     }

     // 正式启动摄像头
     function openMedia(){
         navigator.mediaDevices.getUserMedia(mediaOpts).then(successFunc).catch(errorFunc);
     }

     //关闭摄像头
     function closeMedia(){
         mediaStreamTrack.getVideoTracks().forEach(function (track) {
          track.stop();
          context1.clearRect(0, 0,context1.width, context1.height);//清除画布
         });
     }

     //截取视频
     window.onload=
     function drawMedia(){
         canvas1.setAttribute("width", video.videoWidth);
         canvas1.setAttribute("height", video.videoHeight);
         context1.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);
         img.src = canvas1.toDataURL("image/png");
         var LeftImage = canvas1.toDataURL("image/png");
         var ID=0;
         $.ajax ({
            type:"POST",
            url:"/loginFaceCheck",
            //必须添加 csrf_token
            beforeSend:function (xhr,setting) {
                xhr.setRequestHeader("X-CSRFToken","{{ csrf_token }}");
            },
            dataType:'json',
            data:{
                "id":ID,
                "faceImg":LeftImage
            },
            success:function (displayList) {
                // 处理认证后的数据
                if (displayList.canLogin === true){
                    $('#DisplayNo1').text("验证成功: "+displayList.AuthName).removeClass("label-danger").addClass("" +
                        "label-success");

                     IdentifyNo1 = true;
                     AuthNameNo1 = displayList.AuthName;

                     if (IdentifyNo2 === true){
                         clearTimeout(timeout);
                     }
                     else{
                         // 开始计数，10s内，另一个如果没完成则验证失败
                         timeout = setTimeout(function () {
                         $('#DisplayNo1').text("验证失败: 超时").removeClass("label-success").addClass("label-danger");
                         IdentifyNo1 = false;
                         AuthNameNo1 = '';
                     },10000);
                     }

                    LoginSys(IdentifyNo1 ,AuthNameNo1, IdentifyNo2,AuthNameNo2);
                }
                else{
                    $('#DisplayNo1').text("验证失败: "+displayList.AuthName).removeClass("label-success").addClass("label-danger");

                    IdentifyNo1 = false;
                    AuthNameNo1 = '';
                }
            },
            error:function () {
               $('#DisplayNo1').text("验证失败: 未检测到人脸").removeClass("label-success").addClass("label-danger");

                IdentifyNo1 = false;
                AuthNameNo1 = '';
            }
            })

     }
