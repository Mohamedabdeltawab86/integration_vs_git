import java.util.Scanner;

public class marioBlockSimple {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int n;

        do {
            System.out.println("Enter the number of hashes: ");
            n = input.nextInt();
        }
        while (n<0);

        for (int i=1; i<=n; i++)
        {
            for (int j=1; j<=i; j++)
            {
                System.out.print("#");
            }
            System.out.println();
        }
    }
}

//public class marioBlockSimple {
//
//    public static void main(String[] args) {
//
//        Scanner input = new Scanner(System.in);
//        int n;
//
//        do {
//            System.out.print("Enter the number of lines: ");
//            n = input.nextInt();
//        }
//        while( n<=0 );
//
//        for (int i=1; i<=n; i++)
//        {
//            for (int j=1; j<=i; j++)
//            {
//                System.out.print("*");
//            }
//            System.out.println();
//        }
//
//    }
//}
