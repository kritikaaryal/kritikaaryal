import objectdraw.*;
public class Clicker extends WindowController {
	private Text t;
	private int count; 

	public void begin() {
		count = 0;
		t = new Text("Count = " + count,
				canvas.getWidth()/2,
				canvas.getHeight()/2,
				canvas);
		t.setFontSize(32);
		t.move(-t.getWidth()/2, -t.getHeight()/2);
	}
	public void onMouseClick(Location l) {
		count++;
		t.setText("Count = " + count);
	}
	
	public static void main(String[] args) {
		Clicker c = new Clicker();
		c.startController();
		
	}
}
