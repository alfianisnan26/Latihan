import java.awt.*;
import java.awt.event.*;
import java.text.DecimalFormat;

import javax.swing.*;

public class DivideByZeroTest extends JFrame
   implements ActionListener {

   private JTextField inputField1, inputField2, outputField;
   private int number1, number2;
   double result;

   // set up GUI
   public DivideByZeroTest()
   {
      super( "Demonstrating Exceptions" );

      // get content pane and set its layout
      Container container = getContentPane();
      container.setLayout( new GridLayout( 3, 2 ) );

      // set up label and inputField1
      container.add(
         new JLabel( "Enter numerator ", SwingConstants.RIGHT ) );
      inputField1 = new JTextField();
      container.add( inputField1 );

      // set up label and inputField2; register listener
      container.add( new JLabel( "Enter denominator and press Enter ",
         SwingConstants.RIGHT ) );
      inputField2 = new JTextField();
      container.add( inputField2 );
      inputField2.addActionListener( this );

      // set up label and outputField
      container.add( new JLabel( "RESULT ", SwingConstants.RIGHT ) );
      outputField = new JTextField();
      container.add( outputField );

      setSize( 425, 100 );
      setVisible( true );

   } // end DivideByZeroTest constructor

   // process GUI events
   public void actionPerformed( ActionEvent event )
   {
      outputField.setText( "" );   // clear outputField
      
      DecimalFormat precision3 = new DecimalFormat( "0.000" );

      // read two numbers and calculate quotient
      try {
         number1 = Integer.parseInt( inputField1.getText() );
         number2 = Integer.parseInt( inputField2.getText() );

         result = quotient( number1, number2 );
         //outputField.setText( String.valueOf( result ) );
         outputField.setText( precision3.format( result ) );
      }
          
      // our self-made exception
      catch(DivideByZeroException e)
      {
		  JOptionPane.showMessageDialog(this, "You can not divide by zero!",
		  	"Division By Zero", JOptionPane.ERROR_MESSAGE);
      }

      // process improperly formatted input
      catch ( NumberFormatException numberFormatException ) {
         JOptionPane.showMessageDialog( this,
            "You must enter two integers", "Invalid Number Format",
            JOptionPane.ERROR_MESSAGE );
      }

      // process attempts to divide by zero
      /*
      catch ( ArithmeticException arithmeticException ) {
         JOptionPane.showMessageDialog( this,
            arithmeticException.toString(), "Arithmetic Exception",
            JOptionPane.ERROR_MESSAGE );
      }
      */
      
      /*
      // all exceptions
      catch (Exception e){
      	System.out.println("Something else was caught");	
      }
      */

   } // end method actionPerformed

   // demonstrates throwing an exception when a divide-by-zero occurs
   public double quotient( int numerator, int denominator )
      throws ArithmeticException
   {
	   if ( denominator == 0 )
		   throw new DivideByZeroException();
	   return (double) numerator / denominator;
   }

   public static void main( String args[] )
   {
      DivideByZeroTest application = new DivideByZeroTest();
      application.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );
   }

}