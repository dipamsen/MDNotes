if FORMAT:match 'latex' then
    function Image(elem)
        if string.find(elem.src, "fplogo") then
            return elem
        end
        elem.src = "." .. elem.src
        return elem
    end
end
