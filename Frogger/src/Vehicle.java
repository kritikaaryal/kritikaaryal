import objectdraw.*;
import java.awt.Image;

public class Vehicle extends ActiveObject {
    private VisibleImage vehicleImage;
    private double velocity;
    private double distance;
    private Frog frog;
    private DrawingCanvas canvas;
    private Location vLocation; 
    

    public Vehicle(Image vehiclePic, Location start, double velocity, double distance, Frog frog, DrawingCanvas canvas) {
        this.vehicleImage = new VisibleImage(vehiclePic, start, canvas);
        this.velocity = velocity;
        this.distance = distance;
        this.frog = frog;
        this.canvas = canvas;
        start();
    }

    public void run() {
        double startTime, elapsedTime;
        while (vehicleImage.getX() < distance) {
            startTime = System.currentTimeMillis();
            pause(30);
            elapsedTime = System.currentTimeMillis() - startTime;
            vehicleImage.move(velocity * elapsedTime, 0);

            if (frog.overlaps(vehicleImage)) {
                frog.kill();
            }
        }
        vehicleImage.removeFromCanvas();
    }
}
