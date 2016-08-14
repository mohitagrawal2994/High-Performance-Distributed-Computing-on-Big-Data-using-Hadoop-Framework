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
	print "<script>alert('The User Already Exists.');</script>"
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
        xmlhttp.open("GET", "http://192.168.43.63/cgi-bin/AJAX/testuserexist.py?q=" + str, true);
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
      if(confirm("Proceed To Creating The Account Password"))
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
      top:80px;
      left:750px;
    }
    #cube													/*Styling For Cube*/
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
    .stcube														/*Styling For Hadoop Solutions*/
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
      top:20%;
      left:55%;
      color:black;
    }
    #ptxt
    {
      position:absolute;
      top:31.5%;
      left:55%;
      color:black;
    }
    #p1txt
    {
      position:absolute;
      top:43%;
      left:55%;
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
      <form method="post" action="http://192.168.43.63/cgi-bin/register.py" onsubmit="return chck();" enctype="multipart/form-data" autocomplete="off">
      <b><fieldset style="color:darkblue; border:double; padding:30px;border-radius:0px 40px 0px 40px;"><legend><i>Sign Up</i></legend>
	<pre style="font-family:monaco;font-size:18px;">Fullname                 :   <input type="text" size="30" maxlength="30" id="fname" name="fname" placeholder="Enter Fullname" autofocus="required" required></input><br />
Username                :   <input type="text" size="30" maxlength="30" id="uid" name="uid" onkeyup="username(this.value)" autofocus="required" placeholder="Enter Username" required />
<p id="utxt" name="utxt"></p><br />
Password                 :   <input type="password" size="30" maxlength="30" id="pass1" name="pass1" onkeyup="password(this.value)" placeholder="Enter Password" required />
<p id="ptxt" name="ptxt"></p><br />
Re-Type Password :   <input type="password" size="30" maxlength="30" id="pass2" name="pass2" onkeyup="password1(this.value)" placeholder="Re-type Password" required />
<p id="p1txt" name="p1txt"></p><br />
D.O.B.                      :   <select id="dd" name="dd">
          <option>01</option>
	  <option>02</option>
	  <option>03</option>
	  <option>04</option>
          <option>05</option>
          <option>06</option>
          <option>07</option>
          <option>08</option>
          <option>09</option>
          <option>10</option>
          <option>11</option>
          <option>12</option>
          <option>13</option>
          <option>14</option>
          <option>15</option>
          <option>16</option>
          <option>17</option>
          <option>18</option>
          <option>19</option>
          <option>20</option>
          <option>21</option>
          <option>22</option>
          <option>23</option>
          <option>24</option>
          <option>25</option>
          <option>26</option>
          <option>27</option>
          <option>28</option>
          <option>29</option>
          <option>30</option>
          <option>31</option>
	</select>    <select id="mm" name="mm">
	  <option>01</option>
	  <option>02</option>
	  <option>03</option>
	  <option>04</option>
          <option>05</option>
          <option>06</option>
          <option>07</option>
          <option>08</option>
          <option>09</option>
          <option>10</option>
          <option>11</option>
          <option>12</option>
	</select>    <select id="yy" name="yy">
	  <option>1965</option>
	  <option>1966</option>
	  <option>1967</option>
	  <option>1968</option>
	  <option>1969</option>		
	  <option>1970</option>
	  <option>1971</option>
	  <option>1972</option>
	  <option>1973</option>
       	  <option>1974</option>
          <option>1975</option>
          <option>1976</option>
	  <option>1977</option>
	  <option>1978</option>
          <option>1979</option>
          <option>1980</option>
          <option>1981</option>
          <option>1982</option>
          <option>1983</option>
          <option>1984</option>
          <option>1985</option>
          <option>1986</option>
	  <option>1987</option>
	  <option>1988</option>
	  <option>1989</option>
	  <option>1990</option>
          <option>1991</option>
          <option>1992</option>
          <option>1993</option>
          <option>1994</option>
          <option>1995</option>
          <option>1996</option>
          <option>1997</option>
          <option>1998</option>
	  <option>1999</option>
	  <option>2000</option>
	  <option>2001</option>
	  <option>2002</option>
          <option>2003</option>
          <option>2004</option>
          <option>2005</option>
          <option>2006</option>
          <option>2007</option>
          <option>2008</option>
          <option>2009</option>
          <option>2010</option>
	  <option>2011</option>
	  <option>2012</option>
	  <option>2013</option>
	  <option>2014</option>
          <option>2015</option>
	</select><br />
Gender                     :   Male <input type="radio" id="gen" name="gen" value="Male" required/>  Female <input type="radio" id="gen" name="gen" value="Female" /><br />
Contact                    :   <input type="number" id="ctc" name="ctc" placeholder="Enter Contact" required /><br />
Profile Pic                :   <input type="file" id="pic" name="pic" /><br /><br />
			<input type="submit" style="border-radius:40px;" onclick="return pmt()" />			<input type="reset" style="border-radius:40px;" /></pre>
      </fieldset></b>
      </form>
    </div>

  </body>

</html>"""
