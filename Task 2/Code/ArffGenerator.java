import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.Scanner;

import edu.stanford.nlp.tagger.maxent.*;
 
public class taggerFiles {
    public static void main(String[] args) throws IOException,
            ClassNotFoundException {

    	// Initialize the tagger
        MaxentTagger tagger = new MaxentTagger(
                "taggers/english-left3words-distsim.tagger");
        
		//Input Output Filenames
        FileInputStream stream = new FileInputStream("filename.csv");
    	FileWriter outfile = new FileWriter("output.arff");
    	PrintWriter printer = new PrintWriter(outfile);
    	
		//Creating the file with arff format
    	printer.write("@relation train");
    	printer.write("\n");
    	printer.write("\n");
    	printer.write("@attribute Document string");
    	printer.write("\n");
    	printer.write("@attribute class-rohit {one, two, three, four, five}");
    	printer.write("\n");
    	printer.write("\n");
    	printer.write("@data");
    	printer.write("\n");
    	
    	Scanner sc = new Scanner(stream, "UTF-8");
    	ArrayList list2 = new ArrayList();
	    while (sc.hasNextLine()) {
	        String line = sc.nextLine();	        
	        String sentence = line.split(",")[0];
	        String ratingString = line.split(",")[1];
	        
	        String tokens[] = sentence.split(" ");
	        ArrayList list = new ArrayList();
	        for(String indivtoken : tokens)
	        {	
	        	String tagged = tagger.tagString(indivtoken);
	           	//Set the POS tag
				if(tagged.contains("NN") || tagged.contains("JJR") || tagged.contains("JJS")|| tagged.contains("RB") || tagged.contains("RBR") || tagged.contains("RBS"))
	        	{
	                list.add(tagged.split("_")[0]);
	        	}
	        }
	        LinkedHashSet hash = new LinkedHashSet();
	        hash.addAll(list);
	        list.clear();
	        list.addAll(hash);
	        printer.write("\"");
	        for (int i = 0; i < list.size(); i++) {
	        	
				String res = (String) list.get(i);				
				if(i<(list.size()-1))
					printer.write(res + " ");
				else
					printer.write(res);
	        }
	        printer.write("\"");
	        printer.write("," + ratingString);
	        printer.write("\n");
	    }	    
    	printer.close();
    }
}