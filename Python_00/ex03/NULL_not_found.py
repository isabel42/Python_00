def NULL_not_found(object: any) -> int:

    if bool(object) is False:
    
        match object:
            case bool():
                print("Fake: False",type(object))
            case int():
                print("Zero : 0",type(object))
            case str() :
                print("Empty:",type(object))
            case list():
                print("List empty: ",type(object))
            case tuple():
                print("Tuple empty: ",type(object))
            case dict():
                print("Dict empty: ",type(object))
            case NoneType:
                print("Nothing: None",type(object))

    elif object == object: 
        print("Type not found")
        return 1
    else :
        print("Cheese: nan",type(object))
    return 0

