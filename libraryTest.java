import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
public class LibraryTest{


	@Test
	public void testThatLibraryHasNoBook(){

	//Arrange
	
	Library library = new Library();

	//Act
	int result = library.totalNumberOfBooks();

	//Assert

	assertEquals(result, 0);

}

	@Test
	public void testThatOneBookIsAddedToTheLibraryAndTheTotalNumberOfBookIsOne(){
	
	//Arrange
	
	Library library = new Library();

	//Act
	
	String response = library.addBook("Things fall apart");


	//Assert
	assertEquals(response, "book added successfully");

}

	@Test
	public void ttestThatOneBookIsAddedToTheLibraryAndTheTotalNumberOfBookIsOne(){
	
	//Arrange
	
	Library library = new Library();

	//Act
	
	library.addBook("Things fall apart");
	int result = library.totalNumberOfBooks();


	//Assert
	assertEquals(result, 1);
}
}