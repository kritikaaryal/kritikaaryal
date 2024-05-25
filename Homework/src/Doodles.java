import objectdraw.*;
import java.awt.Color;

public class Doodles extends WindowController{
	
	private Location pressL;
	private Color c;
	
	
	public void begin() {}
	
	public void onMousePress(Location l) {
		pressL = l;
		int r = (int)(Math.random() * 256); 
		int g = (int)(Math.random() * 256); 
		int b = (int)(Math.random() * 256); 
		c = (new Color(r,g,b));
		
	}
	
	public void onMouseDrag(Location l) {
		Line ln = new Line(pressL, l, canvas); 
		ln.setColor(c);
		pressL=l;
	}
	
	public static void main(String[] args) {
		Doodles d = new Doodles(); 
		d.startController(600, 800);
	}

}
