import java.util.*;
import java.sql.*;
import java.rmi.*;
import java.rmi.server.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Vector;
interface DBInterface extends Remote
{
    public String input(String name, LocalDate date, String operation) throws RemoteException;
}

public class Server extends UnicastRemoteObject implements DBInterface
{
    Map<LocalDate, String[]> dateMap = new HashMap<>();
    ResultSet r;
    public Server() throws RemoteException
    { 
        try
        {
            System.out.println("Initializing Server\nServer Ready");
        }
        catch (Exception e)
        {
            System.out.println("ERROR: " +e.getMessage());
        }
    }

    public static void main(String[] args)
    { 
        try
        { 
            Server rs=new Server();
            java.rmi.registry.LocateRegistry.createRegistry(1030).rebind("DBServ", rs);
        }
        catch (Exception e)
        {
            System.out.println("ERROR: " +e.getMessage());
        }
    }

    public String input(String name, LocalDate date, String operation)
    {
        try
        {
            if(operation.equals("Book"))
            {
                if(dateMap.containsKey(date))
                {
                    String[] str = dateMap.get(date);
                    int nextEmptyIndex = -1;
                    for (int i = 0; i < str.length; i++) 
                    {
                        if (str[i] == null) 
                        {
                            nextEmptyIndex = i;
                            break;
                        }
                    }
                    if(nextEmptyIndex != -1) 
                    {
                        (dateMap.get(date))[nextEmptyIndex] = name;
                        return "\nBooking for "+name+" for Date "+date+" has been confirmed.";
                    }
                    else
                    {
                        return "Hotel is full for Date "+date;
                    }
                }
                else
                {
                    String[] strings = {name, "", "", "", "", "", "", "", "", ""};
                    dateMap.put(date, strings);
                    return "\nBooking for "+name+" for Date "+date+" has been confirmed.";
                }
            }
            else if(operation.equals("Cancel"))
            {
                if (dateMap.containsKey(date)) 
                {
                    String[] stringsArray = dateMap.get(date);
        
                    int index = -1;
                    for (int i = 0; i < stringsArray.length; i++) 
                    {
                        if (stringsArray[i] != null && stringsArray[i].equals(name)) 
                        {
                            index = i;
                            break;
                        }
                    }
        
                    if (index != -1) 
                    {
                        stringsArray[index] = "";
                        return "\nCancellation for "+name+" for Date "+date+" on "+date+" is successful.";
                        
                    } else 
                    {
                        return "No bookings available on this date";
                    }
                } 
                else 
                {
                    return "No bookings available on this date";
                }
            }
        }
        catch (Exception e)
        {
            return "ERROR: " +e.getMessage(); 
        }
        return "";
    }
}