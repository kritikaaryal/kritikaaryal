import objectdraw.*;
import java.awt.Color;

public class homework extends WindowController {
    
    private FilledOval circle;
    private FilledRect background;
    
    public void begin() {
        background = new FilledRect(0, 0, canvas.getWidth(), canvas.getHeight(), canvas);
        background.setColor(Color.WHITE);
        
        circle = new FilledOval(canvas.getWidth()/2 - 50, canvas.getHeight()/2 - 50, 100, 100, canvas);
        circle.setColor(Color.RED);
    }
    
    public void onMousePress(Location point) {
        circle.setColor(Color.BLUE);
    }
    
    public void onMouseRelease(Location point) {
        circle.setColor(Color.GREEN);
    }
    
    public void onMouseDrag(Location point) {
        circle.moveTo(point);
    }
    
    public static void main(String[] args) {
        homework window = new homework();
        window.startController(400, 400);
    }
}