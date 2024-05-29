import objectdraw.*;
import java.awt.Image;
import java.util.Random;

public class Lane extends ActiveObject {
    private double velocity;
    private Image vehicleImage;
    private Location startLocation;
    private double distance;
    private Frog frog;
    private DrawingCanvas canvas;
    private Random rand;
 
    public Lane(double speed, Image vehicleImage, Location startLocation, double distance, Frog frog, DrawingCanvas canvas) {
        this.velocity = speed;
        this.vehicleImage = vehicleImage;
        this.startLocation = startLocation;
        this.distance = distance;
        this.frog = frog;
        this.canvas = canvas;
        this.rand = new Random();
        start();	
    }
        
    public void run() {
        while(true) {
            new Vehicle(vehicleImage, startLocation, velocity, distance, frog, canvas);
           
            double vehicleLength = 100;            
            double timeToTravelLength = vehicleLength / velocity;       
            double minTime = 3.0 * timeToTravelLength;            
            double maxTime = 7 * timeToTravelLength;
            double pauseTime = minTime + (maxTime - minTime) * Math.random();
            pause(pauseTime);
        }
    }
}