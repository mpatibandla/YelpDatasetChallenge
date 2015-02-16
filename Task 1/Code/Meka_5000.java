import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;

import weka.classifiers.Evaluation;
import weka.classifiers.bayes.NaiveBayes;
import weka.classifiers.bayes.NaiveBayesMultinomial;
import weka.core.Instances;
import weka.filters.Filter;
import weka.filters.unsupervised.attribute.StringToWordVector;
import meka.classifiers.multilabel.BR;
import meka.classifiers.multilabel.MultilabelClassifier;
import meka.gui.explorer.Explorer;

public class Meka 
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader reader = new BufferedReader(new FileReader("input/reviewtask1_5000.arff"));
		Instances tempset = new Instances(reader);
		PrintWriter printer = new PrintWriter(new FileWriter(new File("output/reviewtask1_5000Res.txt")));
		StringToWordVector stv = new StringToWordVector();
		stv.setInputFormat(tempset);
		Instances dataset = Filter.useFilter(tempset, stv);
		
		NaiveBayes nbm = new NaiveBayes();
		MultilabelClassifier br = new BR();
		br.setClassifier(nbm);
		String[] options = new String[2];
		options[0] = "-W";
		options[1] = "weka.classifiers.bayes.NaiveBayes";
		br.setOptions(options);
		int trainSize = (int) Math.round(dataset.numInstances() * 0.8);
		
		System.out.println("trAIN"+trainSize);
		int testSize = dataset.numInstances() - trainSize;
		Instances train = new Instances(dataset, 0, trainSize-1);
		Instances test = new Instances(dataset, trainSize, testSize);
		
		int cIdx=train.numAttributes()-1;                 
		train.setClassIndex(cIdx);
	    
		br.buildClassifier(train);
		Evaluation eval = new Evaluation(train);
		eval.evaluateModel(br, test);
		printer.write("\n"+eval.toSummaryString("\nResults\n======\n", false));
		printer.close();
	}
}