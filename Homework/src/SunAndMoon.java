import objectdraw.*;
import java.awt.Color;
public class SunAndMoon extends WindowController {
	
	private static final int RADIUS = 100;
	private FilledOval sun;
	private FilledRect sky;
	private FilledRect ground;
	
	public void begin() {
		sun = new FilledOval(canvas.getWidth()/2-RADIUS/2,
				20,
				RADIUS,
				RADIUS,canvas);
		sun.setColor(Color.YELLOW);
		sky = new FilledRect(0,0,
				canvas.getWidth(),
				canvas.getHeight() * 2/3,
				canvas);
		sky.setColor(Color.BLUE);
		
		sun.sendToFront();
		
		ground = new FilledRect(0,
				canvas.getHeight() * 2/3,
				canvas.getWidth(),
				canvas.getHeight() * 1.0/3,
				canvas
				);
		ground.setColor(Color.GREEN);

		Location personLoc = new Location(canvas.getWidth()/2, canvas.getHeight() * 3.0/4);
		person = new StickFigure(personLoc, canvas);	
		person.move(0, -person.getHeight());
		person.setColor(Color.GREEN);
		
	}
		
				
	}
	
	
	public void onMousePress(Location l) {
		//sun.setColor(Color.WHITE);
		//sky.setColor(Color.BLACK);
		//ground.setColor(Color.GRAY);
		
	}
	
	public void onMouseRelease(Location l) {
		//sun.setColor(Color.YELLOW);
		//sky.setColor(Color.BLUE);
		//ground.setColor(Color.GREEN);
	}
	
	public void onMouseDrag(Location l) {
		sun.moveTo(l);
		sun.move(-RADIUS/2, -RADIUS/2);
		if(sun.overlaps(ground)) {
			sun.setColor(Color.WHITE);
			sky.setColor(Color.BLACK);
			ground.setColor(Color.GRAY);
		} else {
			sun.setColor(Color.YELLOW);
			sky.setColor(Color.BLUE);
			ground.setColor(Color.GREEN);
		}
	}
	
	public static void main(String[] args) {
		
		SunAndMoon window = new SunAndMoon();
		window.startController(600, 800);
		
	}

}