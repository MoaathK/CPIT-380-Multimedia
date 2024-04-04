#Describe yourself
#insert your image
#insert some hyperlink
#insert some ordered list
#insert some unordered list
#create a table with three rows and 4 columns
from jes4py import*

def generatePage():
    fileH = open("generate.html","wt")
    fileH.write("""
        <!DOCTYPE html>
<html>
    <head>
        <title>Description About me </title>
    </head>
    <body>
        <h2>Who Am I?</h2>
        <p>My name is moath Alahmadi. Information Technology student with a huge interset in Technology.
            intrested in Web Dev and in Cloud computing. I love watching various sporting event like F1,Football, and other events.
        </p>
        <img src="squared.png" width="150" height="150">
        <a href="https://github.com/MoaathK">My Github Account</a>
        <h3>Best Movies Of All Time</h3>
        <ol>
            <li>Interstellar</li>
            <li>Se7en</li>
            <li>Oppenheimer</li>
            <li>The Shawshank Redemption</li>
            <li>12 Angry Men</li>
          </ol>
          <h3>Best F1 Drivers Of All Time</h3>
          <ul>
            <li>Michael Schumacher</li>
            <li>Lewis Hamilton</li>
            <li>Nicholas Latifi</li>
          </ul>

          <table>
            <tr>
                <td>Days</td>
                <td>one</td>
                <td>two</td>
                <td>Three</td>
            </tr>
            <tr>
                <td>Sunday</td>
                <td>Four</td>
                <td>Five</td>
                <td>Six</td>
            </tr>
            <tr>
                <td>Monday</td>
                <td>Seven</td>
                <td>Eight</td>
                <td>Nine</td>
            </tr>
        </table>
    </body>
</html>
        """)
    fileH.close()
generatePage()