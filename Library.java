public class Library{
		
		int count = 0;

	public int totalNumberOfBooks(){
		
		return count;

}

	public String addBook(String bookTitle){
		count++;
		return "book added successfully";

}
}