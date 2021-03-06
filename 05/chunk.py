#coding:utf-8
class Chunk:
    """
    morphs[] : Morphオブジェクトのリスト
    dst      : 係り先文節インデックス番号
    srcs[]   : 係り受け元文節インデックス番号のリスト
    """
    # コンストラクタ
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    # 文字列を返す
    def __str__(self) -> str:
        sentence = ''
        for i in range(len(self.morphs)):
            sentence = sentence + self.morphs[i].surface
        return sentence + '\t係り先:' + str(self.dst)

    # 文節を返す
    def paragraphs_str(self) -> str:
        paragraphs = ''
        for i in range(len(self.morphs)):
            paragraphs = paragraphs + self.morphs[i].surface
        return paragraphs
    
    # 与えられた品詞が含まれているか返す
    def bool_in_speech(self,speech='') -> bool:
        for i in range(len(self.morphs)):
        # 含まれているなら
            if self.morphs[i].pos in speech:
                return True
        # 含まれていないなら
        return False

    # 与えられた品詞細分類1が含まれているか返す
    def bool_in_speech_detaile(self,speech='') -> bool:
        for i in range(len(self.morphs)):
            # 含まれているなら
            if self.morphs[i].pos1 in speech:
                return True
            # 含まれていないなら
            return False

    # 与えられた文字列が含まれているか返す
    def morph_in_str(self,line='') -> bool:
        for i in range(len(self.morphs)):
            # 含まれているなら
            if self.morphs[i].surface_search(line):
                return True
        return False

    # 文節中で与えられた品詞の部分を最初だけマスクして出力
    # stopはmaskをした時点で止めるかどうか
    def paragraphs_mask_str(self, mask='', speech='', stop=False) -> str:
        # 品詞が指定されていなかったらそのまま出力
        if speech == '':
            return paragrahs_str()
        paragraphs = ''
        mask_flag = False
        for i in range(len(self.morphs)):
            if self.morphs[i].pos and not mask_flag:
                paragraphs += mask
                if stop:
                    return paragraphs
                mask_flag = True
            else:
                paragraphs += self.morphs[i].surface
        return paragraphs
