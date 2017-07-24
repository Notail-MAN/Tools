package util;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ConverterUtil {
	static File file;
	static BufferedReader bufferedReader; 
	public static void fileinput(String filepath){
		System.out.println("filepath: "+filepath);
		file = new File(filepath);
		if(!file.exists()){
			System.out.println("file no exists");
			System.exit(-1);
		}
		return;
	}
	public static void work(){
		System.out.println("fileName: "+file.getName());
		System.out.println("file.length:"+file.length());
		try {
			FileReader fileReader =new FileReader(file);
			bufferedReader = new BufferedReader(fileReader);
			System.out.println("1:"+bufferedReader);
		} catch (Exception e) {
			System.err.println("open error");
			e.printStackTrace();
			System.exit(-2);
		}
		String s;
		StringBuffer stringBuffer = new StringBuffer();
		int linenumber = 0;
		try {
			System.out.println("2:"+bufferedReader);
			while((s = bufferedReader.readLine())!=null){
				s = new String(s.getBytes(),"UTF8");
				if(s.matches("^\\d\\d*$")){
					linenumber++;
					stringBuffer.append("\n"+linenumber+": ");
				}
				if(s.matches("^[a-zA-Z].*")){
					stringBuffer.append(s+" ");
				}
				if(isContainChinese(s)){
					stringBuffer.append(s);
				}
			}
		} catch (Exception e) {
			System.err.println("read error");
			e.printStackTrace();
			System.exit(-3);
		}
		System.out.println("result:");
		System.out.println(stringBuffer.toString());
		
		
	}
	 public static boolean isContainChinese(String str) {
	        Pattern p = Pattern.compile("[\u4e00-\u9fa5]");
	        Matcher m = p.matcher(str);
	        if (m.find()) {
	            return true;
	        }
	        return false;
	    }
	 
	public static void main(String[] args) {
			System.out.println(  isContainChinese("����") );
	
		System.out.println("encoding:"+System.getProperty("file.encoding"));
		Scanner scanner = new Scanner(System.in);
		//fileinput(scanner.nextLine());
		fileinput("E:\\ClassData\\TED\\1");
		work();
		}
}
