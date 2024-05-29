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

            // Assuming the vehicle length is 100 (as per your previous code)
            double vehicleLength = 100;
            // Time it takes for a vehicle to travel its own length
            double timeToTravelLength = vehicleLength / velocity;
            // Ensure a minimum spacing of 1.5 times the vehicle length
            double minTime = 3.0 * timeToTravelLength; 
            // Allow some random variation
            double maxTime = 7 * timeToTravelLength;
            double pauseTime = minTime + (maxTime - minTime) * Math.random();
            pause(pauseTime);
        }
    }
}