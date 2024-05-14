const commentForm = document.forms.commentForm;
const commentFormContent = commentForm.content;
const commentFormParentInput = commentForm.parent;
const commentFormSubmit = commentForm.commentSubmit;
const commentArticleId = commentForm.getAttribute('data-article-id');

commentForm.addEventListener('submit', createComment);

replyUser()

function replyUser() {
    document.querySelectorAll('.btn-reply').forEach(e => {
        e.addEventListener('click', replyComment);
    });
}

function replyComment() {
    const commentUsername = this.getAttribute('data-comment-username');
    const commentMessageId = this.getAttribute('data-comment-id');
    commentFormContent.value = `${commentUsername}, `;
    commentFormParentInput.value = commentMessageId;
}
async function createComment(event) {
    event.preventDefault();
    commentFormSubmit.disabled = true;
    commentFormSubmit.innerText = "Ожидаем ответа сервера";
    try {
        const response = await fetch(`detail/${commentArticleId}/comment_create_view/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'X-Requested-With': 'XMLHttpRequest',
            },
            body: new FormData(commentForm),
        });
        const comment = await response.json();

        let commentTemplate = `<div class="reviews__comment--list margin__left d-flex" id="comment-thread-${comment.id}">
        <div class="reviews__comment--thumbnail">
            <img src="${comment.avatar}" alt="${comment.name}">
        </div>f
        <div class="reviews__comment--content">
            <h4 class="reviews__comment--content__title">${comment.name}</h4>
            <ul class="rating reviews__comment--rating d-flex mb-5">
                <li class="rating__list">
                    <span class="rating__list--icon">
                        <svg class="rating__list--icon__svg" xmlns="http://www.w3.org/2000/svg" width="13.105"
                            height="13.732" viewBox="0 0 10.105 9.732">
                            <path data-name="star - Copy"
                                d="M9.837,3.5,6.73,3.039,5.338.179a.335.335,0,0,0-.571,0L3.375,3.039.268,3.5a.3.3,0,0,0-.178.514L2.347,6.242,1.813,9.4a.314.314,0,0,0,.464.316L5.052,8.232,7.827,9.712A.314.314,0,0,0,8.292,9.4L7.758,6.242l2.257-2.231A.3.3,0,0,0,9.837,3.5Z"
                                transform="translate(0 -0.018)" fill="currentColor">
                            </path>
                        </svg>
                    </span>
                </li>
                <li class="rating__list">
                    <span class="rating__list--icon">
                        <svg class="rating__list--icon__svg" xmlns="http://www.w3.org/2000/svg" width="13.105"
                            height="13.732" viewBox="0 0 10.105 9.732">
                            <path data-name="star - Copy"
                                d="M9.837,3.5,6.73,3.039,5.338.179a.335.335,0,0,0-.571,0L3.375,3.039.268,3.5a.3.3,0,0,0-.178.514L2.347,6.242,1.813,9.4a.314.314,0,0,0,.464.316L5.052,8.232,7.827,9.712A.314.314,0,0,0,8.292,9.4L7.758,6.242l2.257-2.231A.3.3,0,0,0,9.837,3.5Z"
                                transform="translate(0 -0.018)" fill="currentColor">
                            </path>
                        </svg>
                    </span>
                </li>
                <li class="rating__list">
                    <span class="rating__list--icon">
                        <svg class="rating__list--icon__svg" xmlns="http://www.w3.org/2000/svg" width="13.105"
                            height="13.732" viewBox="0 0 10.105 9.732">
                            <path data-name="star - Copy"
                                d="M9.837,3.5,6.73,3.039,5.338.179a.335.335,0,0,0-.571,0L3.375,3.039.268,3.5a.3.3,0,0,0-.178.514L2.347,6.242,1.813,9.4a.314.314,0,0,0,.464.316L5.052,8.232,7.827,9.712A.314.314,0,0,0,8.292,9.4L7.758,6.242l2.257-2.231A.3.3,0,0,0,9.837,3.5Z"
                                transform="translate(0 -0.018)" fill="currentColor">
                            </path>
                        </svg>
                    </span>
                </li>
                <li class="rating__list">
                    <span class="rating__list--icon">
                        <svg class="rating__list--icon__svg" xmlns="http://www.w3.org/2000/svg" width="13.105"
                            height="13.732" viewBox="0 0 10.105 9.732">
                            <path data-name="star - Copy"
                                d="M9.837,3.5,6.73,3.039,5.338.179a.335.335,0,0,0-.571,0L3.375,3.039.268,3.5a.3.3,0,0,0-.178.514L2.347,6.242,1.813,9.4a.314.314,0,0,0,.464.316L5.052,8.232,7.827,9.712A.314.314,0,0,0,8.292,9.4L7.758,6.242l2.257-2.231A.3.3,0,0,0,9.837,3.5Z"
                                transform="translate(0 -0.018)" fill="currentColor">
                            </path>
                        </svg>
                    </span>
                </li>
                <li class="rating__list">
                    <span class="rating__list--icon">
                        <svg class="rating__list--icon__svg" xmlns="http://www.w3.org/2000/svg" width="13.105"
                            height="13.732" viewBox="0 0 10.105 9.732">
                            <path data-name="star - Copy"
                                d="M9.837,3.5,6.73,3.039,5.338.179a.335.335,0,0,0-.571,0L3.375,3.039.268,3.5a.3.3,0,0,0-.178.514L2.347,6.242,1.813,9.4a.314.314,0,0,0,.464.316L5.052,8.232,7.827,9.712A.314.314,0,0,0,8.292,9.4L7.758,6.242l2.257-2.231A.3.3,0,0,0,9.837,3.5Z"
                                transform="translate(0 -0.018)" fill="currentColor">
                            </path>
                        </svg>
                    </span>
                </li>
            </ul>
            <p class="reviews__comment--content__desc">children.message</p>
            <p class="reviews__comment--content__desc" data-comment-id="${comment.id}" data-comment-username="${comment.name}" >Ответить</p>    
            <span class="reviews__comment--content__date">${comment.time_create}</span>
        </div>
    </div>`;
         
        
        if (comment.is_child) {
            document.querySelector(`#comment-thread-${comment.parent_id}`).insertAdjacentHTML("beforeend", commentTemplate);
        }
        else {
            document.querySelector('.nested-comments').insertAdjacentHTML("beforeend", commentTemplate)
        }
        commentForm.reset()
        commentFormSubmit.disabled = false;
        commentFormSubmit.innerText = "Добавить комментарий";
        commentFormParentInput.value = null;
        replyUser();
    }
    catch (error) {
        console.log(error)
    }
}


