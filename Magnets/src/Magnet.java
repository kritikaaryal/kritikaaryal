import objectdraw.DrawingCanvas;
import objectdraw.FramedRect;
import objectdraw.Location;

public class Magnet {
    // Dimensions of the magnet
    private static final double MAGNET_WIDTH = 150;
    private static final double MAGNET_HEIGHT = 50;

    // Box representing the perimeter of the magnet
    private FramedRect box;
    private Pole northPole;
    private Pole southPole;

    // Create a new magnet at location upperLeft
    public Magnet(Location upperLeft, DrawingCanvas canvas) {
        box = new FramedRect(upperLeft, MAGNET_WIDTH, MAGNET_HEIGHT, canvas);
        double x = upperLeft.getX();
        double y = upperLeft.getY();
        northPole = new Pole(this, x + 25, y + MAGNET_HEIGHT / 2, "N", canvas);
        southPole = new Pole(this, x + MAGNET_WIDTH - 25, y + MAGNET_HEIGHT / 2, "S", canvas);
    }

    // Returns the upper-left coordinates of the magnet
    public Location getLocation() {
        return box.getLocation();
    }

    // Move the magnet by the given offset
    public void move(double xoff, double yoff) {
        box.move(xoff, yoff);
        northPole.move(xoff, yoff);
        southPole.move(xoff, yoff);
    }

    // Move the magnet to the given location
    public void moveTo(Location point) {
        double xoff = point.getX() - box.getLocation().getX();
        double yoff = point.getY() - box.getLocation().getY();
        move(xoff, yoff);
    }

    // Check if the given point is within the magnet
    public boolean contains(Location point) {
        return box.contains(point);
    }

    // Returns the width of the magnet
    public double getWidth() {
        return MAGNET_WIDTH;
    }

    // Returns the height of the magnet
    public double getHeight() {
        return MAGNET_HEIGHT;
    }

    // Flip the poles of the magnet
    public void flip() {
        Location northLoc = northPole.getLocation();
        Location southLoc = southPole.getLocation();
        double xOff = southLoc.getX() - northLoc.getX();
        double yOff = southLoc.getY() - northLoc.getY();
        northPole.move(xOff, yOff);
        southPole.move(-xOff, -yOff);
    }

    // Interact with another magnet
  public void interact(Magnet otherMagnet) {
    	
    	if (distance(otherMagnet.getNorth().getLocation(), this.getSouth().getLocation()) < (distance(otherMagnet.getNorth().getLocation(), this.getNorth().getLocation()))) {
    		
    		this.getSouth().attract(otherMagnet.getNorth());
    		
    	}
    	if (distance(otherMagnet.getSouth().getLocation(), this.getNorth().getLocation()) < (distance(otherMagnet.getSouth().getLocation(), this.getSouth().getLocation()))) {
    		
    		this.getNorth().attract(otherMagnet.getSouth());
    		
    	}
    	if (distance(otherMagnet.getSouth().getLocation(), this.getSouth().getLocation()) < (distance(otherMagnet.getSouth().getLocation(), this.getNorth().getLocation()))) {
    		
    		this.getSouth().repel(otherMagnet.getSouth());
    		
    	} else {
    		
    		this.getNorth().repel(otherMagnet.getNorth());
    		
    	}
    	
    }
    
    // Calculate the distance between two locations
    private double distance(Location l1, Location l2) {
        return Math.sqrt(Math.pow(l1.getX() - l2.getX(), 2) + Math.pow(l1.getY() - l2.getY(), 2));
    }

    public Pole getNorth() {
        return northPole;
    }

    public Pole getSouth() {
        return southPole;
    }
}