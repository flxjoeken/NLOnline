document.addEventListener('DOMContentLoaded', () => {
    init_next_btns()
    init_prev_btns()
})

init_prev_btns = function () {
    const prev_btns = document.querySelectorAll('.nl-prev-btn')

    prev_btns.forEach((btn) => {
        btn.addEventListener('click', () => {
            console.log('listeener attached')
            jump_to_prev_form_part()
        })
    })
}

init_next_btns = function () {
    const next_btn = document.querySelectorAll('.nl-next-btn');

    next_btn.forEach((btn) => {
        btn.addEventListener('click', () => {
            const nl_form = document.querySelector('.nl-form')

            if (is_form_part_valid())
                jump_to_next_form_part()
            else
                nl_form.reportValidity()
        })
    })
}


is_form_part_valid = function () {

    const visible_form_part = document.querySelector('.nl-form-group:not(.d-none)')
    const form_elements = visible_form_part.querySelectorAll('input')

    let part_valid = [...form_elements].map((value) => value.validity.valid)

    console.log(part_valid)

    return part_valid.every((value) => value === true)
}

jump_to_next_form_part = function () {
    let form_groups = document.querySelectorAll('.nl-form-group');

    for (let i = 0; i < form_groups.length; i++) {
        if (!form_groups[i].classList.contains('d-none')) {
            form_groups[i].classList.toggle('d-none')
            if (i + 1 <= form_groups.length) {
                form_groups[i + 1].classList.toggle('d-none')
            }
            break
        }
    }
}

jump_to_prev_form_part = function () {
    let form_groups = document.querySelectorAll('.nl-form-group');

    for (let i = 0; i < form_groups.length; i++) {
        if (!form_groups[i].classList.contains('d-none')) {
            form_groups[i].classList.toggle('d-none')
            if (i - 1 <= form_groups.length) {
                form_groups[i - 1].classList.toggle('d-none')
            }
            break
        }
    }
}