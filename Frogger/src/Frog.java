import objectdraw.*;
import java.awt.Image;
import java.awt.Color;

public class Frog {
    private VisibleImage frogImage;
    private Location start;
    private double laneWidth;
    private DrawingCanvas canvas;
    private boolean isAlive;
    private Text ouch; 

    public Frog(Image frogPic, Location start, double laneWidth, DrawingCanvas canvas) {
        this.frogImage = new VisibleImage(frogPic, start, canvas);
        this.start = start;
        this.laneWidth = laneWidth;
        this.canvas = canvas;
        this.isAlive = true;
        this.ouch = null; 
    }

    public void hopToward(Location point) {
        if (isAlive) {
            double frogX = frogImage.getX();
            double frogY = frogImage.getY();
            double hopDistance = laneWidth;

            if (point.getY() < frogY && point.getX() > frogX - hopDistance && point.getX() < frogX + frogImage.getWidth() + hopDistance) {
                frogImage.move(0, -hopDistance);
            } else if (point.getY() > frogY + frogImage.getHeight() && point.getX() > frogX - hopDistance && point.getX() < frogX + frogImage.getWidth() + hopDistance) {
                frogImage.move(0, hopDistance);
            } else if (point.getX() < frogX && point.getY() > frogY - hopDistance && point.getY() < frogY + frogImage.getHeight() + hopDistance) {
                frogImage.move(-hopDistance, 0);
            } else if (point.getX() > frogX + frogImage.getWidth() && point.getY() > frogY - hopDistance && point.getY() < frogY + frogImage.getHeight() + hopDistance) {
                frogImage.move(hopDistance, 0);
            }
        }
    }

    public boolean overlaps(VisibleImage vehicle) {
        return frogImage.overlaps(vehicle);
    }

    public void kill() {
        if (isAlive) {
            isAlive = false;
            frogImage.hide();
            ouch = new Text("OUCH!", frogImage.getX(), frogImage.getY() + frogImage.getHeight() - 20, canvas);
            ouch.setColor(Color.white);
        }
    }

    public void reincarnate() {
        if (!isAlive) {
            isAlive = true;
            frogImage.show();
            frogImage.moveTo(start);
            if (ouch != null) {
                ouch.removeFromCanvas();
                ouch = null;
            }
        }
    }

    public boolean isAlive() {
        return isAlive;
    }
}
