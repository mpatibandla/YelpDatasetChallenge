import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.Random;

import edu.stanford.nlp.ling.Word;
import weka.classifiers.functions.*;
import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.bayes.NaiveBayesMultinomial;
import weka.classifiers.meta.FilteredClassifier;
import weka.core.Instances;
import weka.core.SelectedTag;
import weka.core.converters.ArffSaver;
import weka.core.converters.ConverterUtils.DataSource;
import weka.core.stemmers.LovinsStemmer;
import weka.core.stemmers.Stemmer;
import weka.core.tokenizers.NGramTokenizer;
import weka.core.tokenizers.WordTokenizer;
import weka.filters.Filter;
import weka.filters.unsupervised.attribute.StringToWordVector;


public class Ngrams_LR {
    
	public static void main(String[] args) throws Exception {
		
		File fin = new File("equalRatings.arff");
        File fout = new File("equalRatings_LogisticReg-Bigrams.txt");
        FileInputStream stream = new FileInputStream(fin);
		DataSource datasource = new DataSource(stream);
		FileWriter outfile = new FileWriter(fout);
		PrintWriter printer = new PrintWriter(outfile);
		
		Instances dataset = datasource.getDataSet();
		int seed = 2;
		int folds = 5;
		Random rand = new Random(seed);
		Instances randData = new Instances(dataset);
        randData.setClassIndex(randData.numAttributes()-1);

		randData.randomize(rand);
		randData.stratify(folds);
		
		ArffSaver arffsaver = new ArffSaver();
		arffsaver.setInstances(dataset);
		NGramTokenizer tokenizer = new NGramTokenizer();		
		tokenizer.setNGramMinSize(2);
		tokenizer.setNGramMaxSize(2);
		LibLINEAR liblinear = new LibLINEAR();
		liblinear.setSVMType(new SelectedTag(LibLINEAR.SVMTYPE_L2_LR, LibLINEAR.TAGS_SVMTYPE));
		StringToWordVector stv = new StringToWordVector();
		stv.setTokenizer(tokenizer);
		stv.setWordsToKeep(2500);
		
		FilteredClassifier fc = new FilteredClassifier();
		fc.setClassifier(liblinear);
		fc.setFilter(stv);
		
		Evaluation evalAll = new Evaluation(randData);
		
		for (int n = 0; n < folds; n++) {
			   Evaluation eval1 = new Evaluation(randData);
			   Instances train = randData.trainCV(folds, n);
			   Instances test = randData.testCV(folds, n);
				
			  // build and evaluate classifier
		      Classifier fcCopy = FilteredClassifier.makeCopy(fc);
		      fcCopy.buildClassifier(train);
		      eval1.evaluateModel(fcCopy, test);
		      evalAll.evaluateModel(fcCopy, test);
			  // output evaluation
		      System.out.println();
		      System.out.println("Confusion Matrix for Fold - " + (n+1));
		 }
		printer.write(evalAll.toSummaryString("=== " + folds + "-fold Cross-validation ===", false));
		printer.close();
	}	 
}