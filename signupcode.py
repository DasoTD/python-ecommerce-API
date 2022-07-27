{% load static%}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>

        body {
            background-color: darkcyan;
            background-position: center;
        }

        .all {
            border: 2px solid black;
            margin-left: 350px;
            width: 400px;
            height: 500px;
            
        }
        .formgroup {
            padding: 10px;
            margin: 20px;
            margin-left: 5px;
        }
        .forminline {
            padding: 10px;
            margin: 20px;
        }
        .gender {
            padding: 10px;
            margin: 20px;
        }
        .date {
            padding: 10px;
            margin: 20px;
        }

        .agreed {
            padding: 10px;
            margin: 20px;
        }

        .formgroup input {
            margin: 20px;
        }
        button {
            margin: 20px;
        }
        h3 {
            text-align: center;
            margin-left: 3px;
        }

    </style>
</head>
<body>
  <div class="all">
    <form action="viewproduct.html" method="post" class="content">

        <h3>Sign up to see more of our products </h3>
    
        <div class="formgroup">
    
            <input id="firstname" name="f_name" placeholder="firstname" type="text"  required>
            
            <input id="firstname"  name="l_name"  placeholder= "lastname" type="text"  required>
        </div>
            
            
        <div class="forminline">
            
            <input id="Gmail"  type="gmail"  name="gmail" placeholder="enter your gmail address" required title="it must be atleast 5 digits">
    
        </div>
           
        <div class="gender" name="gender">
    
            <label for="male">male</label>
            <input name="gender" id="male" type="radio" required >
    
            <label for= "female">female</label>
            <input  name="gender" id="female" type="radio" required>
        </div>
    
    
                    <div class="date" name="date">
                        <label>
                            Date of birth:
                     <select>
                    <option>Jan</optiosn>
                    <option>Feb</option>
                    <option>Mar</option>
                    </select>
                    
    
                    
                    
                    day:
                    <select>
                    <option>01</option>
                    <option>02</option>
                    <option>03</option>
                    </select>
    
                    
                    
                     year:
                     <select>
                    <option>2010</option>
                     <option>2011</option>
                    <option>2012</option>
                    </select>
                </label>
                        
                
            </div>
    
            <div class="agreed">
                <label for="agreed">I agreed with the terms and condition</label>
                <input id="agreed" type="radio" required>
                <button><a href="{% url 'viewproduct' %}">submit</a></button>
            </div>
            
    
    </form>

  </div>

</body>
</html>