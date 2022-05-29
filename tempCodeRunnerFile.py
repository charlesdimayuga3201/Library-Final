canvas = Canvas(window,
            bg = "#000000",
            height = 702,
            width = 878,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            878.0,
            702.0,
            fill="#000000",
            outline="")

        background_image = PhotoImage(
        file=relative_to_images("unknown.png"))
        background_label=tk.Label(image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image=background_image 

        entry_image_1 = PhotoImage(
            file=relative_to_images("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            439.5,
            258.0,
            image=entry_image_1
        )
        e1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        e1.place(
            x=260.0,
            y=228.0,
            width=359.0,
            height=58.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_images("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            439.0,
            321.0,
            image=entry_image_2
        )
        e2 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        e2.place(
            x=260.0,
            y=291.0,
            width=358.0,
            height=58.0
        )
        button_image_1 = PhotoImage(
        file=relative_to_images("button_1.png"))
        b1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=loginstd,
            relief="flat"
        )
        b1.place(
            x=251.0,
            y=400.0,
            width=375.0,
            height=71.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_images("button_2.png"))
        b2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=loginadmin,
            relief="flat"
        )
        b2.place(
            x=249.0,
            y=483.0,
            width=375.0,
            height=71.0
        )