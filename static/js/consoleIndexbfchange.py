def consoleIndex(request):
    if 'searchFilter' in request.GET:
        searchFilter = request.GET['searchFilter']
        consoles = [{
            'id': i.id,
            'name': i.name,
            'description': i.description,
            'company': i.company,
            'price': i.price,
            'firstImage': i.consoleimage_set.first().image
        } for i in Console.objects.filter(name__icontains=searchFilter)]
        return JsonResponse({'data': consoles})
    if 'categoryFilter' in request.GET:
        categoryFilter = request.GET['categoryFilter']
        if len(categoryFilter) > 1:
            categoryStr = ""
            for i in range(len(categoryFilter)):
                if i == (len(categoryFilter)-1):
                    categoryStr += categoryFilter[i]
                else:
                    categoryStr += categoryFilter[i] + ","
            categoryFilter = categoryStr.split(",")
            print(categoryFilter)
        consoles = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.consoleimage_set.first().image
        } for x in Console.objects.filter(category_id=categoryFilter)]
        return JsonResponse({'data': consoles})
    context = {'consoles': Console.objects.all()}  #order_by('name')
    return render(request, 'catalog/consoleIndex.html', context)






#upprunalega sem virkar fyrir einn
def consoleIndex(request):
    if 'searchFilter' in request.GET:
        searchFilter = request.GET['searchFilter']
        consoles = [{
            'id': i.id,
            'name': i.name,
            'description': i.description,
            'company': i.company,
            'price': i.price,
            'firstImage': i.consoleimage_set.first().image
        } for i in Console.objects.filter(name__icontains=searchFilter)]
        return JsonResponse({'data': consoles})
    if 'categoryFilter' in request.GET:
        categoryFilter = request.GET['categoryFilter']
        consoles = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.consoleimage_set.first().image
        } for x in Console.objects.filter(category_id=categoryFilter)]
        return JsonResponse({'data': consoles})
    context = {'consoles': Console.objects.all()}  #order_by('name')
    return render(request, 'catalog/consoleIndex.html', context)



###þetta er það sem ég var að reynna vinna með að geta filterað eftir mörgu
def consoleIndex(request):
    if 'searchFilter' in request.GET:
        searchFilter = request.GET['searchFilter']
        consoles = [{
            'id': i.id,
            'name': i.name,
            'description': i.description,
            'company': i.company,
            'price': i.price,
            'firstImage': i.consoleimage_set.first().image
        } for i in Console.objects.filter(name__icontains=searchFilter)]
        return JsonResponse({'data': consoles})
    if 'categoryFilter' in request.GET:
        categoryFilter = request.GET['categoryFilter']
        if len(categoryFilter):
            categoryFilter = categoryFilter.split("_")
            print(categoryFilter)
            consoles = []
            for i in range(len(categoryFilter)):
                for x in Console.objects.filter(category_id=categoryFilter[i]):
                    console = {
                        'id': x.id,
                        'name': x.name,
                        'price': x.price,
                        'categoryID': x.category_id,
                        'firstImage': x.consoleimage_set.first().image
                    }
                    consoles.append(console)
        print(consoles)
        return JsonResponse({'data': consoles})
    context = {'consoles': Console.objects.all()}  #order_by('name')
    return render(request, 'catalog/consoleIndex.html', context)