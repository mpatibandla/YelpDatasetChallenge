import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.Scanner;
import java.io.File;
import edu.stanford.nlp.tagger.maxent.MaxentTagger;
 
public class csvToArffTask1 {
    @SuppressWarnings({ "rawtypes", "unchecked", "resource" })
	public static void main(String[] args) throws IOException,
            ClassNotFoundException {

    	// Initialize the tagger
        MaxentTagger tagger = new MaxentTagger(
              "taggers/english-left3words-distsim.tagger");
        File fin = new File(args[0]);
        File fout = new File(args[1]);
        FileInputStream stream = new FileInputStream(fin);
    	FileWriter outfile = new FileWriter(fout);
    	PrintWriter printer = new PrintWriter(outfile);
    	
    	printer.write("@relation train");
    	printer.write("\n");
    	printer.write("\n");
    	printer.write("@attribute Document string");
    	printer.write("\n");
    	printer.write("@attribute class string");
    	printer.write("\n");
    	printer.write("\n");
    	printer.write("@data");
    	printer.write("\n");
    	
    	Scanner sc = new Scanner(stream, "UTF-8");
    	//ArrayList list2 = new ArrayList();
	    while (sc.hasNextLine()) {
	        String line = sc.nextLine();
	        String sentence = line.split(",")[1];
	        String classattribute = line.split(",")[2];
	        
	        String tokens[] = sentence.split(" ");
	        String classes[] = classattribute.split(" ");
	        ArrayList list1 = new ArrayList();
	        ArrayList list2 = new ArrayList();
	        for(String indivtoken : tokens)
	        {	
	        	String tagged = tagger.tagString(indivtoken);
	        	//if (tagged.substring(tagged.lastIndexOf("_")+1).startsWith("N"))
	        	//if(tagged.contains("JJ") || tagged.contains("JJR") || tagged.contains("JJS") || tagged.contains("RB") || tagged.contains("RBR") || tagged.contains("RBS"))
		       	if(tagged.contains("JJ"))// || tagged.contains("JJR") || tagged.contains("JJS") || tagged.contains("RB") || tagged.contains("RBR") || tagged.contains("RBS"))
	        	{
	                list1.add(tagged.split("_")[0]);
	            }
	        }
	        for(String eachclass : classes)
	        {
	        	list2.add(eachclass);
	        }
	        LinkedHashSet hash1 = new LinkedHashSet();
	        hash1.addAll(list1);
	        list1.clear();
	        list1.addAll(hash1);
	        LinkedHashSet hash2 = new LinkedHashSet();
	        hash2.addAll(list2);
	        list2.clear();
	        list2.addAll(hash2);
	        printer.write("\"");
	        for (int i = 0; i < list1.size(); i++) {
	        	
				String res = (String) list1.get(i);
				//System.out.print(res + " ");
				if(i<(list1.size()-1))
					printer.write(res + " ");
				else
					printer.write(res);
	        }
	        printer.write("\"");
	        printer.write(",");
	        printer.write("\"");
	        for (int i = 0; i < list2.size(); i++) {
	        	
				String res = (String) list2.get(i);
				if(i<(list2.size()-1))
					printer.write(res + " ");
				else
					printer.write(res);
	        }
	        printer.write("\"");
	        printer.write("\n");
	        //System.out.println();
	        //sourceList.add(line);
	    }	    
    	printer.close();

    }
}
