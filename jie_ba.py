# encoding=utf-8
import jieba
import jieba.posseg as pseg #默认词性标注分词器


# jieba.load_userdict('userdict.txt')
# 创建停顿词list
def stopwordslist(filepath): #停顿词库
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

jieba.load_userdict("D:\\Program Files(x86)\\userdict.txt") #自定义词典

# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = pseg.cut(sentence.strip()) #带词性的分词
    stopwords = stopwordslist('D:\Program Files(x86)\stopword.txt')  # 这里加载停顿词的路径
    outstr = ''
    for word, flag in sentence_seged:   #遍历所有分词结果
        if word not in stopwords:   #停顿词检测
            if flag == "eng" or flag == 'v' or flag == 'a' or flag == 'p' or flag == 'm' or flag == 'c':
            #对词性标签筛选
                continue
            else:
                outstr += word + " "+flag   #输出
                outstr += "/"
    return outstr

inputs = open('D:\Program Files(x86)\inputs.txt', 'r', encoding = 'utf-8')    #输入文件路径
outputs = open('D:\Program Files(x86)\output.txt', 'w', encoding='utf-8')     #输出文件
for line in inputs:
    line_seg = seg_sentence(line)  # 这里的返回值是字符串
    #print(line_seg)
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()
