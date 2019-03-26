d = '''
  // The element states
        input; 'picker__input',
        active; 'picker__input--active',

        // The root picker and states *
        picker; 'picker',
        opened; 'picker--opened',
        focused; 'picker--focused',

        // The picker holder
        holder; 'picker__holder',

        // The picker frame, wrapper, and box
        frame; 'picker__frame',
        wrap; 'picker__wrap',
        box; 'picker__box',

        // The picker header
        header; 'picker__header',

        // Month navigation
        navPrev; 'picker__nav--prev',
        navNext; 'picker__nav--next',
        navDisabled; 'picker__nav--disabled',

        // Month & year labels
        month; 'picker__month',
        year; 'picker__year',

        // Month & year dropdowns
        selectMonth; 'picker__select--month',
        selectYear; 'picker__select--year',

        // Table of dates
        table; 'picker__table',

        // Weekday labels
        weekdays; 'picker__weekday',

        // Day states
        day; 'picker__day',
        disabled; 'picker__day--disabled',
        selected; 'picker__day--selected',
        highlighted; 'picker__day--highlighted',
        now; 'picker__day--today',
        infocus; 'picker__day--infocus',
        outfocus; 'picker__day--outfocus',

        // The picker footer
        footer; 'picker__footer',

        // Today, clear, & close buttons
        buttonClear; 'picker__button--clear',
        buttonClose; 'picker__button--close',
        buttonToday; 'picker__button--today'
    '''

# print(type(d))
ss = d.replace(',',';')
print(ss)


