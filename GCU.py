import GCU
while True:
    try:
        GCU.main()
    except SystemExit:
        break
    except Exception:
        pass