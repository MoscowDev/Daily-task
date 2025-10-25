import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;



public class DayTwoTest{


	@Test
	public void testThatCheckReturnsTrueOrFalse(){

	//Arrange
	
	DayTwo convert = new DayTwo();

	//Act
	String result = convert.convertToUpper("BOOK");

	//Assert

	assertEquals(result, "book");

}

}