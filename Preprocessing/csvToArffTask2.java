import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.Scanner;

import edu.stanford.nlp.tagger.maxent.*;
 
public class csvToArffTask2 {
   
	@SuppressWarnings({"resource"})
	public static void main(String[] args) throws IOException,
            ClassNotFoundException {

    	// Initialize the tagger
        MaxentTagger tagger = new MaxentTagger(
                "taggers/english-left3words-distsim.tagger");
        
        FileInputStream stream = new FileInputStream("C:\\Users\\Manasa\\Desktop\\result\\RandomSampleOutput2.csv");
    	FileWriter outfile = new FileWriter("C:\\Users\\Manasa\\Desktop\\result\\task2_result_RS2.arff");
    	PrintWriter printer = new PrintWriter(outfile);
    	
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
    	
	    while (sc.hasNextLine()) {
	        String line = sc.nextLine();
	        String sentence = line.split(",")[1];
	        String ratingNumber = line.split(",")[2];
	        String ratingString;
	        if(ratingNumber.equals("5")) {ratingString = "five";}
	        else if(ratingNumber.equals("4")) {ratingString = "four";}
	        else if(ratingNumber.equals("3")) {ratingString = "three";}
	        else if(ratingNumber.equals("2")) {ratingString = "two";}
	        else {ratingString = "one";}
	        
	        String tokens[] = sentence.split(" ");
	        ArrayList<String> list = new ArrayList<String>();
	        for(String indivtoken : tokens)
	        {	
	        	String tagged = tagger.tagString(indivtoken);
	        	//if (tagged.substring(tagged.lastIndexOf("_")+1).startsWith("N"))
	        	//if(tagged.contains("JJ") || tagged.contains("JJR") || tagged.contains("JJS") || tagged.contains("RB") || tagged.contains("RBR") || tagged.contains("RBS"))
		       	if(tagged.contains("JJ"))// || tagged.contains("JJR") || tagged.contains("JJS") || tagged.contains("RB") || tagged.contains("RBR") || tagged.contains("RBS"))
	        	{
	                list.add(tagged.split("_")[0]);
	            }
	        }
	        LinkedHashSet<String> hash = new LinkedHashSet<String>();
	        hash.addAll(list);
	        list.clear();
	        list.addAll(hash);
	        printer.write("\"");
	        for (int i = 0; i < list.size(); i++) {
	        	
				String res = (String) list.get(i);
				//System.out.print(res + " ");
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