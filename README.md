# An Empirical Study on Capability of Code Large Language Models in Understanding Code Semantics

Large Language Models for Code (Code LLMs) have demonstrated remarkable performance across various software engineering (SE) tasks, increasing the utilization of code LLMs in software development. Despite the success of code LLMs, there remain significant concerns about the actual capabilities of these models, *"whether these models really learn the semantics of code from the training data and leverage the learned knowledge to perform the SE tasks"*. To address these concerns, in this paper, we introduce EMPICA, a comprehensive framework designed to systematically and empirically evaluate the ability of code LLMs in understanding code semantics. Specifically, EMPICA systematically introduces controlled modifications/transformations into the input code and examines the models' responses. Generally, code LLMs must be *robust to semantically equivalent code inputs* and be *sensitive to nonequivalent ones* for all SE tasks.Specifically, for every SE task, given an input code snippet c and its semantic equivalent variants, code LLMs must robustly produce consistent/equivalent outputs while they are expected to generate different outputs for c and its semantic non-equivalent variants. Our experimental results on three representative code understanding tasks, including code summarization, method name prediction, and output prediction, reveal that the robustness and sensitivity of the state-of-the-art code LLMs to code transformations vary significantly across tasks and transformation operators. In addition, the code LLMs exhibit better robustness to the semantic preserving transformation than their sensitivity to the semantic non-preserving transformations. These results highlight a need to enhance the model's capabilities of understanding code semantics, especially the sensitivity property. 


Source code for reproduce experiments can be found [here](https://github.com/ttrangnguyen/EMPICA/)

#### Experimental results for HumanEval Benchmark
1. ###### Code summarization
###### About sematic similarity
<table>
        <thead>
            <tr>
                <th rowspan="2">Transformation Type</th>
                <th rowspan="2">Category</th>
                <th rowspan="2">Subcategory</th>
                <th colspan="4">Java</th>
                <th colspan="4">Python</th>
            </tr>
            <tr>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="4"><b>Robustness to SP Transform.</b></td>
                <td>Control</td>
                <td>Convert For/While</td>
                <td>0.93</td>
                <td>0.95</td>
                <td>0.95</td>
                <td>0.94</td>
                <td>0.90</td>
                <td>0.92</td>
                <td>0.92</td>
                <td>0.93</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Flip IfElse</td>
                <td>0.66</td>
                <td>0.95</td>
                <td>0.94</td>
                <td>0.93</td>
                <td>0.94</td>
                <td>0.95</td>
                <td>0.95</td>
                <td>0.95</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Rename variable</td>
                <td>0.82</td>
                <td>0.93</td>
                <td>0.88</td>
                <td>0.87</td>
                <td>0.84</td>
                <td>0.81</td>
                <td>0.85</td>
                <td>0.85</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Reorder parameters</td>
                <td>0.63</td>
                <td>0.95</td>
                <td>0.93</td>
                <td>0.94</td>
                <td>0.94</td>
                <td>0.90</td>
                <td>0.95</td>
                <td>0.93</td>
            </tr>
            <tr>
                <td rowspan="4"><b>Sensitivity to SNP Transform.</b></td>
                <td>Control</td>
                <td>Negate relational operator</td>
                <td>0.07</td>
                <td>0.05</td>
                <td>0.06</td>
                <td>0.06</td>
                <td>0.05</td>
                <td>0.07</td>
                <td>0.05</td>
                <td>0.05</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Remove conditional statement</td>
                <td>0.11</td>
                <td>0.09</td>
                <td>0.12</td>
                <td>0.11</td>
                <td>0.11</td>
                <td>0.09</td>
                <td>0.11</td>
                <td>0.11</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Replace arithmetic operator</td>
                <td>0.40</td>
                <td>0.07</td>
                <td>0.08</td>
                <td>0.09</td>
                <td>0.07</td>
                <td>0.12</td>
                <td>0.09</td>
                <td>0.08</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Remove def statement</td>
                <td>0.10</td>
                <td>0.07</td>
                <td>0.09</td>
                <td>0.11</td>
                <td>0.08</td>
                <td>0.12</td>
                <td>0.09</td>
                <td>0.10</td>
            </tr>
        </tbody>
    </table>

###### About lexical similarity

<table>
        <thead>
            <tr>
                <th rowspan="2">Transformation Type</th>
                <th rowspan="2">Category</th>
                <th rowspan="2">Subcategory</th>
                <th colspan="4">Java</th>
                <th colspan="4">Python</th>
            </tr>
            <tr>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="4"><b>Robustness to SP Transform.</b></td>
                <td>Control</td>
                <td>Convert For/While</td>
                <td>0.87</td>
                <td>0.83</td>
                <td>0.89</td>
                <td>0.87</td>
                <td>0.84</td>
                <td>0.76</td>
                <td>0.97</td>
                <td>0.84</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Flip IfElse</td>
                <td>0.71</td>
                <td>0.86</td>
                <td>0.86</td>
                <td>0.87</td>
                <td>0.90</td>
                <td>0.83</td>
                <td>0.90</td>
                <td>0.90</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Rename variable</td>
                <td>0.78</td>
                <td>0.77</td>
                <td>0.80</td>
                <td>0.79</td>
                <td>0.77</td>
                <td>0.62</td>
                <td>0.78</td>
                <td>0.76</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Reorder parameters</td>
                <td>0.70</td>
                <td>0.83</td>
                <td>0.85</td>
                <td>0.86</td>
                <td>0.87</td>
                <td>0.77</td>
                <td>0.88</td>
                <td>0.87</td>
            </tr>
            <tr>
                <td rowspan="4"><b>Sensitivity to SNP Transform.</b></td>
                <td>Control</td>
                <td>Negate relational operator</td>
                <td>0.11</td>
                <td>0.16</td>
                <td>0.13</td>
                <td>0.13</td>
                <td>0.11</td>
                <td>0.18</td>
                <td>0.11</td>
                <td>0.11</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Remove conditional statement</td>
                <td>0.17</td>
                <td>0.27</td>
                <td>0.20</td>
                <td>0.20</td>
                <td>0.21</td>
                <td>0.29</td>
                <td>0.20</td>
                <td>0.21</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Replace arithmetic operator</td>
                <td>0.33</td>
                <td>0.20</td>
                <td>0.15</td>
                <td>0.17</td>
                <td>0.14</td>
                <td>0.29</td>
                <td>0.15</td>
                <td>0.15</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Remove def statement</td>
                <td>0.16</td>
                <td>0.24</td>
                <td>0.17</td>
                <td>0.20</td>
                <td>0.16</td>
                <td>0.29</td>
                <td>0.17</td>
                <td>0.19</td>
            </tr>
        </tbody>
    </table>

2. ###### Method Name Prediction
###### About exactly match
<table>
        <thead>
            <tr>
                <th rowspan="2">Transformation Type</th>
                <th rowspan="2">Category</th>
                <th rowspan="2">Subcategory</th>
                <th colspan="4">Java</th>
                <th colspan="4">Python</th>
            </tr>
            <tr>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="4"><b>Robustness to SP Transform.</b></td>
                <td>Control</td>
                <td>Convert For/While</td>
                <td>0.81</td>
                <td>0.71</td>
                <td>0.72</td>
                <td>0.85</td>
                <td>0.42</td>
                <td>0.53</td>
                <td>0.60</td>
                <td>0.53</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Flip IfElse</td>
                <td>0.59</td>
                <td>0.46</td>
                <td>0.80</td>
                <td>0.83</td>
                <td>0.47</td>
                <td>0.41</td>
                <td>0.53</td>
                <td>0.67</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Rename variable</td>
                <td>0.40</td>
                <td>0.37</td>
                <td>0.34</td>
                <td>0.52</td>
                <td>0.32</td>
                <td>0.18</td>
                <td>0.32</td>
                <td>0.36</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Reorder parameters</td>
                <td>0.56</td>
                <td>0.59</td>
                <td>0.72</td>
                <td>0.63</td>
                <td>0.53</td>
                <td>0.49</td>
                <td>0.66</td>
                <td>0.66</td>
            </tr>
            <tr>
                <td rowspan="4"><b>Sensitivity to SNP Transform.</b></td>
                <td>Control</td>
                <td>Negate relational operator</td>
                <td>0.47</td>
                <td>0.57</td>
                <td>0.55</td>
                <td>0.41</td>
                <td>0.54</td>
                <td>0.54</td>
                <td>0.62</td>
                <td>0.50</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Remove conditional statement</td>
                <td>0.65</td>
                <td>0.65</td>
                <td>0.61</td>
                <td>0.62</td>
                <td>0.70</td>
                <td>0.54</td>
                <td>0.72</td>
                <td>0.67</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Replace arithmetic operator</td>
                <td>0.57</td>
                <td>0.72</td>
                <td>0.51</td>
                <td>0.56</td>
                <td>0.70</td>
                <td>0.66</td>
                <td>0.65</td>
                <td>0.63</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Remove def statement</td>
                <td>0.32</td>
                <td>0.53</td>
                <td>0.49</td>
                <td>0.47</td>
                <td>0.38</td>
                <td>0.58</td>
                <td>0.61</td>
                <td>0.45</td>
            </tr>
        </tbody>
    </table>

  ###### F1-Score

  <table>
        <thead>
            <tr>
                <th rowspan="2">Transformation Type</th>
                <th rowspan="2">Category</th>
                <th rowspan="2">Subcategory</th>
                <th colspan="4">Java</th>
                <th colspan="4">Python</th>
            </tr>
            <tr>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="4"><b>Robustness to SP Transform.</b></td>
                <td>Control</td>
                <td>Convert For/While</td>
                <td>0.90</td>
                <td>0.89</td>
                <td>0.85</td>
                <td>0.93</td>
                <td>0.67</td>
                <td>0.80</td>
                <td>0.82</td>
                <td>0.77</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Flip IfElse</td>
                <td>0.78</td>
                <td>0.72</td>
                <td>0.91</td>
                <td>0.94</td>
                <td>0.70</td>
                <td>0.76</td>
                <td>0.80</td>
                <td>0.82</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Rename variable</td>
                <td>0.61</td>
                <td>0.72</td>
                <td>0.62</td>
                <td>0.74</td>
                <td>0.55</td>
                <td>0.44</td>
                <td>0.62</td>
                <td>0.63</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Reorder parameters</td>
                <td>0.71</td>
                <td>0.83</td>
                <td>0.88</td>
                <td>0.79</td>
                <td>0.67</td>
                <td>0.77</td>
                <td>0.81</td>
                <td>0.82</td>
            </tr>
            <tr>
                <td rowspan="4"><b>Sensitivity to SNP Transform.</b></td>
                <td>Control</td>
                <td>Negate relational operator</td>
                <td>0.25</td>
                <td>0.26</td>
                <td>0.30</td>
                <td>0.20</td>
                <td>0.32</td>
                <td>0.23</td>
                <td>0.31</td>
                <td>0.24</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Remove conditional statement</td>
                <td>0.41</td>
                <td>0.35</td>
                <td>0.42</td>
                <td>0.44</td>
                <td>0.47</td>
                <td>0.31</td>
                <td>0.44</td>
                <td>0.42</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Replace arithmetic operator</td>
                <td>0.36</td>
                <td>0.39</td>
                <td>0.34</td>
                <td>0.36</td>
                <td>0.50</td>
                <td>0.38</td>
                <td>0.38</td>
                <td>0.37</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Remove def statement</td>
                <td>0.17</td>
                <td>0.26</td>
                <td>0.25</td>
                <td>0.24</td>
                <td>0.25</td>
                <td>0.26</td>
                <td>0.30</td>
                <td>0.25</td>
            </tr>
        </tbody>
    </table>
   
4. ###### Output Prediction
<table>   
<thead>
            <tr>
                <th rowspan="2">Transformation Type</th>
                <th rowspan="2">Category</th>
                <th rowspan="2">Subcategory</th>
                <th colspan="4">Java</th>
                <th colspan="4">Python</th>
            </tr>
            <tr>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="4"><b>Robustness to SP Transform.</b></td>
                <td>Control</td>
                <td>Convert For/While</td>
                <td>0.75</td>
                <td>0.69</td>
                <td>0.78</td>
                <td>0.80</td>
                <td>0.69</td>
                <td>0.69</td>
                <td>0.57</td>
                <td>0.63</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Flip IfElse</td>
                <td>0.70</td>
                <td>0.66</td>
                <td>0.68</td>
                <td>0.68</td>
                <td>0.70</td>
                <td>0.70</td>
                <td>0.52</td>
                <td>0.67</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Rename variable</td>
                <td>0.54</td>
                <td>0.59</td>
                <td>0.62</td>
                <td>0.60</td>
                <td>0.62</td>
                <td>0.47</td>
                <td>0.51</td>
                <td>0.49</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Reorder parameters</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td rowspan="4"><b>Sensitivity to SNP Transform.</b></td>
                <td>Control</td>
                <td>Negate relational operator</td>
                <td>0.35</td>
                <td>0.46</td>
                <td>0.38</td>
                <td>0.41</td>
                <td>0.33</td>
                <td>0.44</td>
                <td>0.50</td>
                <td>0.46</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Remove conditional statement</td>
                <td>0.43</td>
                <td>0.49</td>
                <td>0.52</td>
                <td>0.57</td>
                <td>0.48</td>
                <td>0.52</td>
                <td>0.62</td>
                <td>0.61</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Replace arithmetic operator</td>
                <td>0.44</td>
                <td>0.51</td>
                <td>0.51</td>
                <td>0.49</td>
                <td>0.37</td>
                <td>0.47</td>
                <td>0.62</td>
                <td>0.59</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Remove def statement</td>
                <td>0.36</td>
                <td>0.43</td>
                <td>0.50</td>
                <td>0.41</td>
                <td>0.31</td>
                <td>0.44</td>
                <td>0.54</td>
                <td>0.55</td>
            </tr>
        </tbody>
    </table>

  For the detail responses of Code LLMs for the orignal program and the transformed code of the HumanEval benchmark, you can find [here](https://drive.google.com/drive/folders/1T7E_8EuvzhHGkHR5eMaIY0yjbn6eu3k0?usp=sharing).

#### Experimental results for MPBB
1. ##### Code summarization
###### About semantic similarity
<table>
        <thead>
            <tr>
                <th rowspan="2">Transformation Type</th>
                <th rowspan="2">Category</th>
                <th rowspan="2">Subcategory</th>
                <th colspan="4">Python</th>
            </tr>
            <tr>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="4"><b>Robustness to SP Transform.</b></td>
                <td>Control</td>
                <td>Convert For/While</td>
                <td>0.90</td>
                <td>0.93</td>
                <td>0.93</td>
                <td>0.91</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Flip IfElse</td>
                <td>0.93</td>
                <td>0.94</td>
                <td>0.95</td>
                <td>0.93</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Rename variable</td>
                <td>0.79</td>
                <td>0.81</td>
                <td>0.80</td>
                <td>0.81</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Reorder parameters</td>
                <td>0.95</td>
                <td>0.91</td>
                <td>0.94</td>
                <td>0.95</td>
            </tr>
            <tr>
                <td rowspan="4"><b>Sensitivity to SNP Transform.</b></td>
                <td>Control</td>
                <td>Negate relational operator</td>
                <td>0.06</td>
                <td>0.08</td>
                <td>0.05</td>
                <td>0.05</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Remove conditional statement</td>
                <td>0.09</td>
                <td>0.12</td>
                <td>0.09</td>
                <td>0.11</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Replace arithmetic operator</td>
                <td>0.07</td>
                <td>0.12</td>
                <td>0.08</td>
                <td>0.09</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Remove def statement</td>
                <td>0.08</td>
                <td>0.13</td>
                <td>0.10</td>
                <td>0.10</td>
            </tr>
        </tbody>
    </table>
    
###### About lexical similarity

<table>
        <thead>
            <tr>
                <th rowspan="2">Transformation Type</th>
                <th rowspan="2">Category</th>
                <th rowspan="2">Subcategory</th>
                <th colspan="4">Python</th>
            </tr>
            <tr>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="4">Robustness to SP Transform.</td>
                <td>Control</td>
                <td>Convert For/While</td>
                <td>0.85</td>
                <td>0.82</td>
                <td>0.87</td>
                <td>0.83</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Flip IfElse</td>
                <td>0.89</td>
                <td>0.84</td>
                <td>0.88</td>
                <td>0.87</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Rename variable</td>
                <td>0.73</td>
                <td>0.63</td>
                <td>0.71</td>
                <td>0.71</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Reorder parameters</td>
                <td>0.89</td>
                <td>0.78</td>
                <td>0.88</td>
                <td>0.87</td>
            </tr>
            <tr>
                <td rowspan="4">Sensitivity to SNP Transform.</td>
                <td>Control</td>
                <td>Negate relational operator</td>
                <td>0.11</td>
                <td>0.18</td>
                <td>0.11</td>
                <td>0.12</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Remove conditional statement</td>
                <td>0.17</td>
                <td>0.28</td>
                <td>0.19</td>
                <td>0.21</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Replace arithmetic operator</td>
                <td>0.13</td>
                <td>0.24</td>
                <td>0.14</td>
                <td>0.16</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Remove def statement</td>
                <td>0.14</td>
                <td>0.31</td>
                <td>0.19</td>
                <td>0.20</td>
            </tr>
        </tbody>
    </table>
    
2. ##### Method Name Prediction
###### About exactly match
<table>
        <thead>
            <tr>
                <th rowspan="2">Transformation Type</th>
                <th rowspan="2">Category</th>
                <th rowspan="2">Subcategory</th>
                <th colspan="4">Python</th>
            </tr>
            <tr>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="4">Robustness to SP Transform.</td>
                <td>Control</td>
                <td>Convert For/While</td>
                <td>0.52</td>
                <td>0.64</td>
                <td>0.62</td>
                <td>0.78</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Flip IfElse</td>
                <td>0.50</td>
                <td>0.58</td>
                <td>0.65</td>
                <td>0.67</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Rename variable</td>
                <td>0.20</td>
                <td>0.16</td>
                <td>0.16</td>
                <td>0.21</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Reorder parameters</td>
                <td>0.61</td>
                <td>0.61</td>
                <td>0.71</td>
                <td>0.72</td>
            </tr>
            <tr>
                <td rowspan="4">Sensitivity to SNP Transform.</td>
                <td>Control</td>
                <td>Negate relational operator</td>
                <td>0.53</td>
                <td>0.57</td>
                <td>0.47</td>
                <td>0.53</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Remove conditional statement</td>
                <td>0.64</td>
                <td>0.68</td>
                <td>0.62</td>
                <td>0.62</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Replace arithmetic operator</td>
                <td>0.61</td>
                <td>0.68</td>
                <td>0.63</td>
                <td>0.66</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Remove def statement</td>
                <td>0.50</td>
                <td>0.58</td>
                <td>0.64</td>
                <td>0.55</td>
            </tr>
        </tbody>
    </table>
    
###### About F1-Score

<table>
        <thead>
            <tr>
                <th rowspan="2">Transformation Type</th>
                <th rowspan="2">Category</th>
                <th rowspan="2">Subcategory</th>
                <th colspan="4">Python</th>
            </tr>
            <tr>
                <th>Code Llama</th>
                <th>GPT-3.5</th>
                <th>DeepSeek</th>
                <th>MagicCoder</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="4">Robustness to SP Transform.</td>
                <td>Control</td>
                <td>Convert For/While</td>
                <td>0.70</td>
                <td>0.85</td>
                <td>0.83</td>
                <td>0.87</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Flip IfElse</td>
                <td>0.68</td>
                <td>0.79</td>
                <td>0.81</td>
                <td>0.79</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Rename variable</td>
                <td>0.36</td>
                <td>0.42</td>
                <td>0.38</td>
                <td>0.36</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Reorder parameters</td>
                <td>0.76</td>
                <td>0.84</td>
                <td>0.85</td>
                <td>0.86</td>
            </tr>
            <tr>
                <td rowspan="4">Sensitivity to SNP Transform.</td>
                <td>Control</td>
                <td>Negate relational operator</td>
                <td>0.32</td>
                <td>0.27</td>
                <td>0.26</td>
                <td>0.28</td>
            </tr>
            <tr>
                <td>Control</td>
                <td>Remove conditional statement</td>
                <td>0.43</td>
                <td>0.39</td>
                <td>0.38</td>
                <td>0.42</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Replace arithmetic operator</td>
                <td>0.42</td>
                <td>0.39</td>
                <td>0.38</td>
                <td>0.43</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Remove def statement</td>
                <td>0.32</td>
                <td>0.33</td>
                <td>0.35</td>
                <td>0.34</td>
            </tr>
        </tbody>
    </table>

3. ##### Output Prediction

 <table>
      <thead>
          <tr>
              <th rowspan="2">Transformation Type</th>
              <th rowspan="2">Category</th>
              <th rowspan="2">Subcategory</th>
              <th colspan="4">Python</th>
          </tr>
          <tr>
              <th>Code Llama</th>
              <th>GPT-3.5</th>
              <th>DeepSeek</th>
              <th>MagicCoder</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td rowspan="4">Robustness to SP Transform.</td>
              <td>Control</td>
              <td>Convert For/While</td>
              <td>0.67</td>
              <td>0.82</td>
              <td>0.53</td>
              <td>0.47</td>
          </tr>
          <tr>
              <td>Control</td>
              <td>Flip IfElse</td>
              <td>0.63</td>
              <td>0.77</td>
              <td>0.62</td>
              <td>0.49</td>
          </tr>
          <tr>
              <td>Data</td>
              <td>Rename variable</td>
              <td>0.46</td>
              <td>0.63</td>
              <td>0.40</td>
              <td>0.31</td>
          </tr>
          <tr>
              <td>Data</td>
              <td>Reorder parameters</td>
              <td>0.55</td>
              <td>0.65</td>
              <td>0.44</td>
              <td>0.37</td>
          </tr>
          <tr>
              <td rowspan="4">Sensitivity to SNP Transform.</td>
              <td>Control</td>
              <td>Negate relational operator</td>
              <td>0.42</td>
              <td>0.37</td>
              <td>0.54</td>
              <td>0.60</td>
          </tr>
          <tr>
              <td>Control</td>
              <td>Remove conditional statement</td>
              <td>0.52</td>
              <td>0.38</td>
              <td>0.60</td>
              <td>0.69</td>
          </tr>
          <tr>
              <td>Data</td>
              <td>Replace arithmetic operator</td>
              <td>0.57</td>
              <td>0.56</td>
              <td>0.74</td>
              <td>0.78</td>
          </tr>
          <tr>
              <td>Data</td>
              <td>Remove def statement</td>
              <td>0.43</td>
              <td>0.38</td>
              <td>0.66</td>
              <td>0.68</td>
          </tr>
      </tbody>
  </table>

  For the detail responses of Code LLMs for the orignal program and the transformed code of the MBPP benchmark, you can find [here](https://drive.google.com/drive/folders/1Ldwd3dJUN26__WzeSRNkbp1QacLulYot?usp=sharing).
