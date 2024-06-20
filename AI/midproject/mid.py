from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 載入預訓練的 GPT-2 模型和分詞器
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# 設置模型為生成模式
model.eval()

def chatbot(input_text):
    # 將輸入文本轉換為模型可接受的輸入格式
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # 生成回應
    with torch.no_grad():
        outputs = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# 主程式
if __name__ == '__main__':
    print("你可以開始和 AI 女友對話了！輸入 '退出' 以結束對話。")

    while True:
        user_input = input("你：")

        if user_input.lower() == '退出':
            print("AI 女友已關閉。")
            break

        response = chatbot(user_input)
        print("AI 女友：", response)
