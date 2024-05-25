import objectdraw.*;
import java.awt.Color;

public class StickFigure {
	
	// Class Constants
	private double HEAD_SIZE = 50;
	private double BODY_LENGTH = 100;
	private double LEG_LENGTH = 50;
	
	// State = instance variables
	private Line rArm, lArm;
	private Line torso;
	private FilledOval head;
	private Line rLeg, lLeg;
	private StickFigure person1;
	private StickFigure person2;
	
	// Behavior = methods
	public StickFigure(Location l, DrawingCanvas c) {
		this(l.getX(), l.getY(), c);
	}
	Location personLoc = new Location(canvas.getWidth()/2, canvas.getHeight() * 3.0/4);
	person = new StickFigure(personLoc, canvas);	
	person.move(0, -person.getHeight());
	person.setColor(Color.GREEN);
	
}
	
	// Constructor = make new objects
	public StickFigure(double x, double y, DrawingCanvas c) {
		head = new FilledOval(x, y, HEAD_SIZE, HEAD_SIZE, c);
		Location start = new Location(x+HEAD_SIZE/2, 
									  y+HEAD_SIZE);
		Location end = new Location(start.getX(), 
									start.getY() + BODY_LENGTH);
		torso = new Line(start, end, c);
		
		start = end;
		end = new Location(start.getX() + LEG_LENGTH,
							start.getY() + LEG_LENGTH);
		rLeg = new Line(start, end, c);
		
		end = new Location(start.getX() - LEG_LENGTH,
				start.getY() + LEG_LENGTH);
		
		lLeg = new Line(start, end, c);
		
		start = new Location(x+HEAD_SIZE/2, 
				  y+HEAD_SIZE+BODY_LENGTH/2);
		
		end = new Location(start.getX() + LEG_LENGTH,
				start.getY() - LEG_LENGTH);
		
		rArm = new Line(start, end, c);
		
		end = new Location(start.getX() - LEG_LENGTH,
				start.getY() - LEG_LENGTH);
		
		lArm = new Line(start, end, c);
		
		Color t = new Color(163, 131,62);
		setColor(t);
	}
	
	// Accessor Methods = get the state of the object
	public double getHeight() {
		return rLeg.getEnd().getY() - head.getLocation().getY();
	}
	
	// Mutator Methods = change the state of the object
	public void move(double dx, double dy) {
		head.move(dx, dy);
		torso.move(dx, dy);
		rLeg.move(dx, dy);
		lLeg.move(dx, dy);
		rArm.move(dx, dy);
		lArm.move(dx, dy);
	}
	
	public void setColor(Color c) {
		head.setColor(c);
		torso.setColor(c);
		rLeg.setColor(c);
		lLeg.setColor(c);
		rArm.setColor(c);
		lArm.setColor(c);
	}
}
