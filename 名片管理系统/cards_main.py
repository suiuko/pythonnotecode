import cards_tools

while True: # 无限循环，用用户主动决定什么时候退出
    
    cards_tools.show_menu()
    # TODO(小明) 显示功能菜单

    action_str = input("请选择需要执行的操作：")
    print("您选择的操作是 %s" %action_str)

    # 1，2，3 针对名片的操作

    if action_str in ["1","2","3"]:
        
        #新增名片
        if action_str == "1":
            cards_tools.new_card()
            # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
            # 查询名片
        elif action_str =="3":
            cards_tools.search_card()
        pass

    # 0 退出系统
    elif action_str == "0":

        print("欢迎再次使用")
        break
        # 如果在开发时不希望立刻编写内部的代码
        # 可以使用pass，表示一个占位符，运行不会有操作
        #pass 
        
    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择")
