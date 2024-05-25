import objectdraw.Location;
import objectdraw.WindowController;

public class MagnetGame extends WindowController {
    private Magnet magnet1;
    private Magnet magnet2;
    private Magnet movingMagnet;
    private Location start; 

    
	public void begin() {
        magnet1 = new Magnet(new Location(100, 100), canvas);
        magnet2 = new Magnet(new Location(300, 100), canvas);
    }


	public void onMousePress(Location point) {
		start = point; 
        if (magnet1.contains(point)) {
            movingMagnet = magnet1;
        } else if (magnet2.contains(point)) {
            movingMagnet = magnet2;
        }
    }
	 

	public void onMouseDrag(Location point) {
        if (movingMagnet != null) {
            movingMagnet.move(point.getX() - start.getX(), point.getY() - start.getY());
        	start = point; 
            
            Magnet otherMagnet = (movingMagnet == magnet1) ? magnet2 : magnet1;
            movingMagnet.interact(otherMagnet);
        } else {
        	movingMagnet =  null;
        }
    }

    
	public void onMouseClick(Location point) {
        if (magnet1.contains(point)) {
            magnet1.flip();
            magnet1.interact(magnet2);
        } else if (magnet2.contains(point)) {
            magnet2.flip();
            magnet2.interact(magnet1);
        }
    }
	public void onMouseRelease(Location point) {
		movingMagnet = null; 
	}

    public static void main(String[] args) {
        new MagnetGame().startController(500, 500);
    }
}