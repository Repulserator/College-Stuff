import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class PhoneBook 
{
 public static void main(String[] args) 
 {
displayMenu();
}
public static void callcontact(String name)
{
String s[] = findNumber(name);
if(s !=null)
System.out.println("calling" + name + " at " +s[1]);
else
System.out.println("No person found named " + name);
}
public static void savecontact(String name, long number)
{
System.out.println("saving contact " + name + " : " + number);
try (PrintWriter pw = new PrintWriter(new FileWriter("file.txt",true)))
{
pw.println(name +":" + number);
}
catch(IOException e) 
{
System.out.println(e.getMessage());
}
}

public static String[] findNumber(String name)
{
try(Scanner in = new Scanner(new File("C:\\Users\\Acer\\OneDrive\\Desktop\\PhoneBook.txt")))
{
String[] s = new String[0];
boolean foundPerson = false;
while(in.hasNextLine()) 
{
s= in.nextLine().split(":");
if(s[0].equals(name))
{
System.out.println("the number associated with " + name + " is " + s[1]);
foundPerson = true;
break;
}
}
if(!foundPerson)
{
System.out.println("could not find" + name);
s=null;
}
return s;
}
catch(IOException e) 
{
System.out.println(e.getMessage());
}
return null;
}
public static void displayMenu() 
{
try (Scanner in = new Scanner(System.in))
{
String name;
do
{
System.out.println("What would you like to do? (1, 2, 3... etc)");

System.out.println("1 Call contact");
System.out.println("2 Save contact");
System.out.println("3 Find Number");
//break this later 
int choice = in.nextInt();
in.nextLine();
switch (choice)
{
case 1:
System.out.println("Who would you like to call? (Firstname Lastname)");
name = in.nextLine();
callcontact (name);
break;
case 2:
System.out.println("What is the name of the person would you like to save? (Firstname Lastname)");
name = in.nextLine();
System.out.println("What is the phone number of person you are saving? (1234567897)");
long number = in.nextLong();
in.nextLine();
savecontact (name, number);
break;
case 3:
System.out.println("What is the name of the person whose phone number you are searching? (Firstname Lastname) ");
findNumber(in.nextLine());
break;
default:
break;
}
System.out.println("Do you wish to perform another action? (Y/N)");
if(in.next().toLowerCase().charAt(0) != 'Y')
break;
}
while(true);
}
 catch (Exception e) 
{
System.out.println(e.getMessage());
}
}
}