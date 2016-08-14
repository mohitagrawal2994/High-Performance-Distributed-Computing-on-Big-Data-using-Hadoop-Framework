#!/usr/bin/python

import cgi

print "Content-type:text/html"
x=cgi.FieldStorage()
q=x.getvalue('q')
print ""

print """<!DOCTYPE html>
  <head>"""
if(q == 'perror'):
	print "<script>alert('The Passwords Do Not Match');</script>"
if(q == 'ferror'):
	print "<script>alert('The Form Content Are Not Appropriate');</script>"
if(q == 'merror'):
	print "<script>alert('The Username or Contact Specified For It Does Not Exist.');</script>"
print """  <script>
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
    function password1(str)											/* AJAX For 2nd Password */
    {
      var xmlhttp = new XMLHttpRequest();
      if(str == "")
        document.getElementById("p1txt").innerHTML = "";
      else
      {
        xmlhttp.onreadystatechange = function()
        {
          if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
          {
            document.getElementById("p1txt").innerHTML = xmlhttp.responseText;
          }
        };
      xmlhttp.open("GET", "http://192.168.43.63/cgi-bin/AJAX/testpass.py?q=" + str, true);
      xmlhttp.send();
      }
    }
    function pmt()
    {
      var a = document.getElementById('pass1').value;
      var b = document.getElementById('pass2').value;
      var c = 0 ;
      if((a.length>=6)&&(b.length>=6))
      {
        if( a != b )
        {
	  alert('Entered Passwords Do Not Match');       	
	  c = 1;
        }
      }
      else
      {
	alert("The Password Should Be A Minimum Of 6 characters")
	c = 1;
      }
      var x = document.getElementById('ctc').value;
      if(!((x<10000000000)&&(x>999999999)))
      {
        alert("The Phone No. Entered Is Not A Valid One") ;
        c = 1 ;
      }
      if(c==1)
      {
        return false ;
      }
    }
    function chck()
    {
      if(confirm("Proceed To Resetting The Account Password"))
	return true ;
      else
	return false ;
    }
    function cb()
    {
	document.location="http://192.168.43.63/cgi-bin/index.py?q=0"
    }
  </script>
  <style>
    #fm														/* Styling For Position Of Form */
    {
      position:absolute;
      top:150px;
      left:750px;
    }
    #cube
    {
      position:absolute;
      top:250px;
      left:160px;
      perspective:280px;
      perspective-origin:50% 50%;
    }
    #cube1
    {
      position:relative;
      margin:auto;
      height:180px;
      width:180px;
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
      height:140px;
      width:140px;
      padding:20px;
      background-color:rgba(0, 0, 0, 0.5);
      border:2px solid red;
    }
    #f1
    {
      transform: rotateX(90deg) translateZ(90px);
    }
    #f2
    {
      transform: translateZ(90px);
    }
    #f3
    {
      transform: rotateY(90deg) translateZ(90px);
    }
    #f4
    {
      transform: rotateY(180deg) translateZ(90px);
    }
    #f5
    {
      transform: rotateY(-90deg) translateZ(90px);
    }
    #f6
    {
      transform: rotateX(-90deg) translateZ(90px) rotate(180deg);
    }
    .stcube
    {
      font-family:cooper black;
      font-size:25px;
      color:white;
      position:relative;
      top:35%;
      left:5%;
    }
    .stcube1
    {
      font-family:cooper black;
      font-size:25px;
      color:white;
      position:relative;
      top:35%;
      left:25%;
    }
    #utxt
    {
      position:absolute;
      top:18%;
      left:52%;
      color:black;
    }
    #ptxt
    {
      position:absolute;
      top:45%;
      left:52%;
      color:black;
    }
    #p1txt
    {
      position:absolute;
      top:61%;
      left:52%;
      color:black;
    }
  </style>
  </head>
  
  <body style="background: url('http://192.168.43.63/backgrounds/Body1.jpg') no-repeat top right;">
    <div id="cube" name="cube" onclick="cb()">
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
      <form method="post" action="http://192.168.43.63/cgi-bin/forgot.py" onsubmit="return chck();" autocomplete="off">
      <b><fieldset style="color:darkblue; border:double; padding:30px;border-radius:0px 40px 0px 40px;"><legend><i>Restore</i></legend>
	<pre style="font-family:monaco;font-size:18px;">
Username                :   <input type="text" size="30" maxlength="30" id="uid" name="uid" placeholder="Enter Username" onkeyup="username(this.value)" autofocus="required"/>
<p id="utxt" name="utxt"></p><br />
Contact                    :   <input type="number" id="ctc" name="ctc" placeholder="Enter Contact For Verification" /><br />
Password                 :   <input type="password" size="30" maxlength="30" id="pass1" name="pass1" placeholder="Enter Password" onkeyup="password(this.value)"/>
<p id="ptxt" name="ptxt" ></p><br />
Re-Type Password :   <input type="password" size="30" maxlength="30" id="pass2" name="pass2" placeholder="Re-type Password" onkeyup="password1(this.value)"/>
<p id="p1txt" name="p1txt" ></p><br /><br />
			<input type="submit" style="border-radius:40px;" />			<input type="reset" style="border-radius:40px;" /></pre>
      </fieldset></b>
      </form>
    </div>

  </body>

</html>"""
