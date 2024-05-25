import objectdraw.*;
import java.awt.Color;

public class LaundrySorter extends WindowController {
    private FramedRect white;
    private FramedRect black;
    private FramedRect color;
    private int count;
    private Text whiteText;
    private Text blackText;
    private Text colorText;
    private Location start;
    private FilledRect swatch;
    private Text correct;
    private Text incorrect;
    private int cCount;
    private int iCount;
    private Color c;
    private Location pressLocation;
    private boolean dragging;

    public void begin() {
        white = new FramedRect(55, 200, 80, 80, canvas);
        whiteText = new Text("whites", 75, 230, canvas);
        whiteText.setFontSize(15);

        black = new FramedRect(160, 200, 80, 80, canvas);
        blackText = new Text("darks", 180, 230, canvas);
        blackText.setFontSize(15);

        color = new FramedRect(265, 200, 80, 80, canvas);
        colorText = new Text("colors", 285, 230, canvas);
        colorText.setFontSize(15);

        swatch = new FilledRect(160, 100, 60, 60, canvas);
        c = generateRandomColor();
        swatch.setColor(c);
        start = swatch.getLocation();

        correct = new Text("Correct = " + cCount, 50, 100, canvas);
        correct.setFontSize(15);

        incorrect = new Text("Incorrect = " + iCount, 50, 80, canvas);
        incorrect.setFontSize(15);
    }

    private Color generateRandomColor() {
        int r = (int) (Math.random() * 256);
        int g = (int) (Math.random() * 256);
        int b = (int) (Math.random() * 256);
        return new Color(r, g, b);
    }

    public void onMousePress(Location l) {
        pressLocation = l;
        if (swatch.contains(l)) {
            dragging = true;
        }
    }
    public void onMouseDrag(Location l) {
        if (dragging) {
            swatch.move(l.getX() - pressLocation.getX(), l.getY() - pressLocation.getY());
            pressLocation = l;
        }
    }

    public void onMouseRelease(Location l) {
        int sum = c.getRed() + c.getGreen() + c.getBlue();
        boolean correctLocation = false;
        if (sum < 230 && swatch.overlaps(black)) {
        	correctLocation = true;
        } else if (sum > 600 && swatch.overlaps(white)) {
        	correctLocation = true;
        } else if (swatch.overlaps(color)) {
        	correctLocation = true;
        }

        if (correctLocation) {
        	c = generateRandomColor();
            cCount++;
            
            swatch.setColor(c);
        }
          else if (swatch.getX() < 55 || swatch.getX() > 345 || swatch.getY() < 200 || swatch.getY() > 280) {
            swatch.moveTo(start);	
            } else {
            iCount++;
        }

        swatch.moveTo(start);
        correct.setText("Correct = " + cCount);
        incorrect.setText("Incorrect = " + iCount);
        dragging = false;
    }

    public static void main(String[] args) {
        LaundrySorter c = new LaundrySorter();
        c.startController();
    }
}