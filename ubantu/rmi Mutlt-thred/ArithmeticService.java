import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ArithmeticService extends Remote {
    double add(double a, double b) throws RemoteException;
    double subtract(double a, double b) throws RemoteException;
    double multiply(double a, double b) throws RemoteException;
    double divide(double a, double b) throws RemoteException;
}

// chage  the  ip adress first  by ifconfig or  ip -all
// javac *.java
// rmiRegistry 
// new terminal
// java ArithmeticServer
// new terminl
//java ArithmeticClient