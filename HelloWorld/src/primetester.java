import java.until.Scanner;
public class primetester {

	public static boolean isPrime(int x) {
		double sqrt = Math.sqrt(x);
		if (x==2) return true;
		if (x<2 || x%2==0)
			return false;
		for(int i=3; i <= sqrt; i+=2) {
			if(x%i ==0) {
				return false;
			}
		}
		return true;
	}
	
	 public static void main(String[] args) {
		 System.out.print("Enter a number: ");
		 Scanner s = new Scanner(System.in);
		 int number = scanner.nextInt();
		 if (isPrime(n)) {
			 Systemout.println(n + "is not prime.");
		 }
	 }
	     