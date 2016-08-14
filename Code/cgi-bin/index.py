#!/usr/bin/python

import cgi
print "Content-type:text/html"
x=cgi.FieldStorage()
q=x.getvalue('q')
print ""
print """<!DOCTYPE html>
  <head>"""
if(q == 'ferror'):
	print "<script>alert('The Form Content Are Not Appropriate');</script>"
if(q == 'merror'):
	print "<script>alert('There Was Some Database Error.');</script>"
if(q == 'regsucess'):
	print "<script>alert('Your Account Was Created Sucessfully');</script>"
if(q == 'forgsucess'):
	print "<script>alert('Your Password Was Changed Sucessfully');</script>"
if(q == 'accsucess'):
	print "<script>alert('Your Account Was Deleted Sucessfully');</script>"
if(q == '1'):
	print "<script>alert('Your Have Been Sucessfully Logged Out');</script>"
    
print """<script> 
      function username(str)											/* AJAX For Username */
      {
      var xmlhttp = new XMLHttpRequest();
      if(str == "")
        document.getElementById("utxt").innerHTML = "";
      else
      {
        xmlhttp.onreadystatechange = function()
        {
          if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
          {
            document.getElementById("utxt").innerHTML = xmlhttp.responseText;
          }
        };
        xmlhttp.open("GET", "http://192.168.43.63/cgi-bin/AJAX/testuser.py?q=" + str, true);
        xmlhttp.send();
      }
    }
    function password(str)											/* AJAX For Password */
    {
      var xmlhttp = new XMLHttpRequest();
      if(str == "")
        document.getElementById("ptxt").innerHTML = "";
      else
      {
        xmlhttp.onreadystatechange = function()
        {
          if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
          {
            document.getElementById("ptxt").innerHTML = xmlhttp.responseText;
          }
        };
      xmlhttp.open("GET", "http://192.168.43.63/cgi-bin/AJAX/testpass.py?q=" + str, true);
      xmlhttp.send();
      }
    }  
  </script>
  <style>
    #fm														/* Styling For Position Of Form */
    {
      position:absolute;
      top:230px;
      left:500px;
    }
    #cube													/* Styling For Cube */
    {
      position:absolute;
      top:50px;
      left:630px;
      perspective:280px;
      perspective-origin:50% 50%;
    }
    #cube1
    {
      position:relative;
      margin:auto;
      height:140px;
      width:140px;
      transform-style:preserve-3d;
      transform:rotateX(0deg) rotateY(45deg);	
      animation:move 5s infinite
    }
    @keyframes move
    {
      from{transform:rotateY(0deg)}
      50%{transform:rotateY(90deg)}
      to{transform:rotateY(0deg)}
    }
    .face 
    {
      position:absolute;
      height:100px;
      width:100px;
      padding:20px;
      background-color:rgba(0, 0, 0, 0.5);
      border:2px solid red;
    }
    #f1
    {
      transform: rotateX(90deg) translateZ(70px);
    }
    #f2
    {
      transform: translateZ(70px);
    }
    #f3
    {
      transform: rotateY(90deg) translateZ(70px);
    }
    #f4
    {
      transform: rotateY(180deg) translateZ(70px);
    }
    #f5
    {
      transform: rotateY(-90deg) translateZ(70px);
    }
    #f6
    {
      transform: rotateX(-90deg) translateZ(70px) rotate(180deg);
    }
    .stcube
    {
      font-family:cooper black;
      font-size:23px;
      color:white;
      position:relative;
      top:30%;
      left:-13%;
    }
    .stcube1
    {
      font-family:cooper black;
      font-size:25px;
      color:white;
      position:relative;
      top:30%;
      left:10%;
    }
    #cntct													/* Styling For Contact */
    {
      position:absolute;
      top:86%;
      left:9%;
      width:80%;
      height:8%;
      padding:20px;
      border-radius: 40px 40px 0px 0px;
      background-color:rgba(0,255,0,0.5);
    }
    #abt
    {
      position:absolute;
      top:88%;
      left:85%;
      width:5%;
      height:5%;
    }
    #utxt
    {
      position:absolute;
      top:26%;
      left:45%;
      color:black;
    }
    #ptxt
    {
      position:absolute;
      top:51%;
      left:45%;
      color:black;
    }
  </style>
  </head>

  <body style="background: url('http://192.168.43.63/backgrounds/Body1.jpg') no-repeat top right;">
    <div id="cube" name="cube">
    <div id="cube1" name="cube1">
      <div class="face" id="f1">
      </div>
      <div class="face" id="f2">
	<span class="stcube">SoLuTiOns</span>
      </div>
      <div class="face" id="f3">
      </div>
      <div class="face" id="f4">
      </div>
      <div class="face" id="f5">
	<span class="stcube1">Ha2uP</span>
      </div>
      <div class="face" id="f6">
      </div>
    </div>
    </div>
    <div id="fm" name="fm">
    <form method="post" action="http://192.168.43.63/cgi-bin/login.py" autocomplete="off">
      <b><fieldset style="color:darkblue; border:double; padding:30px;border-radius:0px 40px 0px 40px;"><legend><i>Sign In</i></legend>
        Username : <input type="text" size="30" maxlength="30" id="uid" name="uid" placeholder="Enter Username" onkeyup="username(this.value)" autofocus="required" required /><br />
        <p id="utxt" name="utxt" ></p><br /><br />
        Password &nbsp: <input type="password" size="30" maxlength="30" id="pass1" name="pass1" placeholder="Enter Password" onkeyup="password(this.value)" required />
        <p id="ptxt" name="ptxt" ></p><br /><br /><br /><br />
        <input type="submit" style="margin-left:60px; border-radius:40px;" />
        <input type="reset" style="margin-left:60px; border-radius:40px;" />
      </fieldset></b>
    </form>
    <a href="http://192.168.43.63/cgi-bin/reg.py" style="position:absolute; left:30px; top:280px; margin-left:10px;color:black;"><b><i>Create An Account</i></b></a>
    <a href="http://192.168.43.63/cgi-bin/forg.py" style="position:absolute; left:190px; top:280px; margin-left:30px;color:black;"><b><i>Forgot Your Password<strong></i></b></a>
    </div>
    <div id="cntct" name="cntct">Owner : Mohit Kumar Agrawal, Kavita Rana<br /><br />LinkedIn : <br />GitHub :</div>
    <div id="abt" name="abt"><a href="http://192.168.43.63/about.html">About</a></div>
  </body>

</html>"""
