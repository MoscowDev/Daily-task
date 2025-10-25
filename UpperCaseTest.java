import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;



public class UpperCaseTest{


	@Test
	public void testThatStringConvertsToUpperCase(){

	//Arrange
	
	UpperCase convert = new UpperCase();

	//Act
	String result = convert.convertToUpper("BOOK");

	//Assert

	assertEquals(result, "book");

}

}