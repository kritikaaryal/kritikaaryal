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
    private double ymin = 0;
    

    public Lane(double speed, Image vehicleImage, Location startLocation, double distance, Frog frog, DrawingCanvas canvas, double velocity) {
        this.velocity = velocity;
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
			
		}
	}
}